

from be_mongo_adapter.data_access.mongo_adapter.mongo_adapter import MongoAdapter
from be_mongo_adapter.data_access.mongo_adapter.mongo_adapter_error import MongoAdapterException

_client = None


def _create_client(host, port):
    global _client
    if _client is None:
        _client = MongoAdapter(host, port)


def get_client(host=None, port=27017):
    global _client

    if _client is None and host is not None:
        _create_client(host, port)
    elif _client is None and host is None:
        raise MongoAdapterException('There is no mongo connection already open', None)

    if _client is not None:
        return _client
