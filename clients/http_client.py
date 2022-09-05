import requests

class HTTPClient:

    def __init__(self, url):
        self.__session = requests.session()
        self.__url = url

        pass

    @property
    def source(self):
        return self.__url

    def get(self, name):
        r = self.__session.get(self.__url + '/' + name.replace('.', '/'))
        if r.status_code != 200:
            return None
        return r.text