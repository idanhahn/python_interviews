from mongokit.connection import MongoClient


class MongoAdapter:

    def __init__(self, host='localhost', port=27017):
        self._client = MongoClient(host=host, port=port, connect=False)
