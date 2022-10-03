from dataclasses import dataclass

from clients.http_client import HTTPClient


@dataclass
class TransportCatalog:
    http: HTTPClient = HTTPClient
