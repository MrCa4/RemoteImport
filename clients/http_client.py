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
        target = self.__url + '/' + name.replace('.', '/')
        req_without_ext = self.__session.get(target)
        if req_without_ext.status_code == 200 \
                and req_without_ext.headers.get('Content-type') == 'text/html' \
                and len(req_without_ext.content) != 0 \
                and '__all__' in req_without_ext.text:
            return req_without_ext.content
        req_with_ext = self.__session.get(target+EXTENTION)
        if req_with_ext.status_code == 200 \
                and len(req_with_ext.content) != 0 \
                and req_with_ext.headers.get('Content-type') != 'text/plain':
            return req_with_ext.content
        return None

