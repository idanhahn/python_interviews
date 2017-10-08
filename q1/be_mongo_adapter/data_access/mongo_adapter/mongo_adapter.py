from logging import getLogger

from copy import deepcopy
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# todo: support multi collections in one query
from be_common.enums.common import ENTITY_ID
from be_mongo_adapter.data_access.mongo_adapter.mongo_adapter_error import MongoAdapterException


class MongoAdapter:
    """
    MongoController is a wrapper for PyMongo
    """

    def __init__(self, host='localhost', port=27017) -> None:
        """
        Initializes the mongo client

        :param str host:
        :param int port:
        """
        super().__init__()
        self._logger = getLogger(__name__)
        self._client = MongoClient(host=host, port=port, connect=False)
        try:
            result = self._client.admin.command("ismaster")
            self._logger.info("Connected to mongodb ip:{}, port: {}".format(host, port))
        except ConnectionFailure as e:
            print("Server not available, error: {}".format(e))
            raise MongoAdapterException("Error while trying to connect mongo", e)


    def insert(self, db, collection, documents):
        pass

    def _insert_one(self, db, collection, document):

        if self._client is None:
            raise MongoAdapterException("Client is not initialize", None)

        if document is None:
            raise MongoAdapterException("No document to insert", None)

        self._client[db][collection].insert_one(
            document=document,
        )

    def _insert_many(self, db, collection, documents):

        if self._client is None:
            raise MongoAdapterException("Client is not initialize", None)

        if documents is None:
            raise MongoAdapterException("No document to insert", None)

        self._client[db][collection].insert_many(
            documents=documents,
            ordered=True,
        )

    def update(self, db, collection, documents):
        pass

    def _update_one(self, db, collection, document):
        pass

    def _update_many(self, db, collection, documents):
        pass

