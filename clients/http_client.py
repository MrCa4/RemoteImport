import requests

EXTENTION = ".py"


class HTTPClient:

    def __init__(self, url):
        self.__session = requests.session()
        self.__url = url
        pass

    @property
    def source(self):
        return self.__url

    def get(self, name):
        target = self.__url + '/' + name.replace('.', '/') + EXTENTION
        r = self.__session.get(target)
        if r.status_code != 200 or r.headers.get('Content-type') != 'text/plain' or len(r.content) == 0:
            return None
        return r.content
