
import remote_import_core

remote_import_core.init('http', url="http://127.0.0.1:9000")

from foo.bar import module


print(module.a)
print(module.abc)
