import importlib.util
import sys
from importlib.abc import MetaPathFinder


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
        exec(self.current_module_code, new_module.__dict__)
        sys.modules[spec.name] = new_module
        return new_module


def init(transport):
    sys.meta_path.append(RemoteImport(transport))
