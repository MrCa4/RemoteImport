import importlib.util
import sys
from dataclasses import dataclass
from importlib.abc import MetaPathFinder
from transport_catalog import TransportCatalog


@dataclass
class TransportChoice(TransportCatalog):

    def __init__(self, transport, *args, **kwargs):
        self.transport_obj = self.__getattribute__(transport)(*args, **kwargs)


class RemoteImport(MetaPathFinder):
    session = None

    def __init__(self, transport):
        if RemoteImport.session is None:
            RemoteImport.session = transport
        self.current_module_code: str = ""

    def find_module(self, name, path=None):
        remote_code = RemoteImport.session.get(name)
        if remote_code is not None:
            self.current_module_code = remote_code
        return self

    def load_module(self, name):
        spec = importlib.util.spec_from_loader(name, loader=None, origin=RemoteImport.session.source, is_package=True)
        new_module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = new_module
        exec(self.current_module_code, new_module.__dict__)
        return new_module


def init(transport, *args, **kwargs):
    sys.meta_path.append(RemoteImport(TransportChoice(transport, *args, **kwargs).transport_obj))
