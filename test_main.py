
import remote_import_core

remote_import_core.init('http', url="http://127.0.0.1:9000")

from foo.bar import module
#

print(module.aba)
module.a_aa.test1()
module.aaa.test()
