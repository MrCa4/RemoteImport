# Dynamic Remote Import

Dynamic remote import is an extensible python module
that allows you to import packages (modules, classes,
methods and functions, etc.) from remote repositories
directly into RAM.

Perhaps it will be useful when deploying code in
centralized code repositories and downloading new updates
to runtime. For example, if you have a service in a
container, it can reload modules after the expiration 
of time or on command without restarting the container.
___
![](https://img.shields.io/badge/python-3.10-blueviolet)
![](https://img.shields.io/github/last-commit/MrCa4/RemoteImport?color=blueviolet)
![](https://img.shields.io/github/issues-pr/MrCa4/RemoteImport?color=blueviolet)
![](https://img.shields.io/github/forks/MrCa4/RemoteImport?style=social)
---
## Small explanations

This module implies an extension.
To do this, it is divided into two entities:
1. Import Core
2. Transport

The "import core" can work with any transport object satisfying certain conditions, 
so you can write your own transport.
To add your own transport module, you need:
1. Implement "get" method or function in it, 
which takes the name of the module and returns 
either None, if nothing is found, or a string or 
bytestring representing python code.
Please remember, the way to search for modules in python
(https://docs.python.org/3/reference/import.html#searching).
2. Save your transport module to the "clients" folder.
3. Add the module definition to the "transport_catalog" module.

___
## Installation
Use the git to install remote import.
```bash
git clone https://github.com/MrCa4/RemoteImport.git
```
___
## Usage Dynamic Import

Import remote import core module

For Example:
```python
from remote_import import remote_import_core
```
Select the transport and the necessary parameters
```python
remote_import_core.init('http', url="http://127.0.0.1:9000")
```
Import necessary module.
```python
from foo.bar import module
```
---
## Supported import string formats
```python
from foo.bar import module
from foo.bat import aa, bb
from foo.bat.aa import test as t
from foo.bas import *
```
---
## Supported import transport

HTTP/HTTPS, SMB

---
## HTTP/HTTPS storage requirements

1. Response with python obj(class, method function, etc) data must contain
"Content-type" header:
```python
text/plain
```
2. When mask import is used, You must add index.html in package dir
on the similarity of the file ```"__init__"```, For example:
```python
index.html

__all__ = ["a_aa", "a_bb"]
```

For tests use simple http server:
```python
python -m http.server 9000
```
___
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
___ 
## License
[MIT](https://choosealicense.com/licenses/mit/)