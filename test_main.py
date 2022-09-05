
import remote_import_core

#TODO auto start import module
#TODO more simple transport adding
from clients.http_client import HTTPClient
remote_import_core.init(HTTPClient('http://localhost:9000'))




import module
#TODO in http client use specifiec headers to get text/or download data and parse
#from foo.bar import module


print(module.a)
#print 1 - ok
