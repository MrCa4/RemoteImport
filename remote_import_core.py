import base64
import importlib.util
import sys
from importlib.abc import MetaPathFinder


class RemoteImport(MetaPathFinder):
    session = None

    def __init__(self, transport):
        self.transport = transport
        self.current_module_code: str = None

    def find_module(self, name, path=None):
        print(name)
        new_library = self.transport.get(name)
        if new_library is not None:
            self.current_module_code = base64.b64decode(new_library)
            return self

    def load_module(self, name):
        spec = importlib.util.spec_from_loader(name, loader=None, origin=self.transport.source, is_package=True)
        new_module = importlib.util.module_from_spec(spec)
        exec(self.current_module_code, new_module.__dict__)
        sys.modules[spec.name] = new_module
        return new_module

sys.meta_path.append(RemoteImport("http"))
# if __name__ == '__main__':
#
#     pass