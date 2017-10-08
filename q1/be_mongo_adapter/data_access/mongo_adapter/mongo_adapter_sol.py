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

        if self._client is None:
            raise MongoAdapterException("Client is not initialize", None)

        if documents is None:
            raise MongoAdapterException("No document to insert", None)

        '''
            add logic here
        '''

        if len(documents) == 1:
            self._insert_one(
                db=db,
                collection=collection,
                document=documents,
            )
        else:
            self._insert_many(
                db=db,
                collection=collection,
                documents=documents,
            )







    '''
        Private methods here
    '''

    def _insert_one(self, db, collection, document):


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

    ''' 
        def update(self, db, collection, documents)
        def _update_one(self, db, collection, document)
        def _update_many(self, db, collection, documents)
    '''

    def _update_one(self, db, collection, document):

        self._client[db][collection].update_one(
            filter={'id': document['id']},
            update={'$set': document},
            upsert=True,
        )






    def upsert(self, db, collection, document):
        """
        Inserts documents to the collection inside db

        :param str db:  db name
        :param str collection: collection name
        :param document: document to upsert
        :return documents with mongo ids
        """
        if self._client is None:
            raise MongoAdapterException("Client is not initialize", None)

        if document is None:
            raise MongoAdapterException("No document to insert", None)

        document_to_insert = deepcopy(document)
        upsert_result = self._client[db][collection].update_one({'id': document_to_insert[ENTITY_ID]},
                                                                {"$set": document_to_insert}, True).upserted_id

        # if we have some documents that not inserted successfully
        if upsert_result is None:
            raise MongoAdapterException("Document upsert failed, document:{}"
                                        .format(document_to_insert), None)

        return document

    def find_one(self, db, collection, original_query_document=None, unfiltered=False):
        """
        Finds the first document with the query_document filter

        :param str db: db name
        :param str collection: collection name
        :param original_query_document:document filter
        :param unfiltered: unfiltered by is_deleted and time
        :return result: None or the document
        """
        results = self.find(db, collection, original_query_document, unfiltered)
        return results[0] if len(results) > 0 else None

    def find(self, db, collection, original_query_document=None, unfiltered=False):
        """
        Finds all documents with the query_document filter

        :param str db:  db name
        :param str collection: collection name
        :param original_query_document: document filter
        :param unfiltered: unfiltered by is_deleted and time
        :return results array: documents after conversion to waycare hash
        """
        if self._client is None:
            raise MongoAdapterException("Client is not initialize", None)

        if unfiltered:
            results = self._client[db][collection].find(original_query_document)
            return list(results)
        else:
            query_document = self._build_query_document(original_query_document)
            results = self._client[db][collection].find(query_document)
            return list(results)

    def find_by_distance(self, db, collection, location, additional_query=None,
                         location_field_name="location", min_distance=0, max_distance=1000):
        """
        Return documents in radius

        :param additional_query:
        :param location_field_name:
        :param str db:  db name
        :param str collection: collection name
        :param location: a point which is in the center of the location - an array of lng[0] and lat[1]
        :param min_distance:
        :param max_distance:
        :return: array of documents or None
        """
        if self._client is None:
            raise MongoAdapterException("Client is not initialize", None)

        geo_query_document = {
            location_field_name: {
                "$nearSphere": {
                    "$geometry": location,
                    "$maxDistance": max_distance,
                    "$minDistance": min_distance
                }
            }
        }
        query_document = self._build_query_document(geo_query_document, additional_query)

        try:
            results = self._client[db][collection].find(query_document)
        except Exception as e:
            raise MongoAdapterException("query failed", errors=e)

        return list(results)

    def close(self):
        """
        Close a connection

        :return: nothing, a void function
        """
        if self._client is not None:
            self._logger.info("Closed connection to mongodb")
            self._client.close()

    def update(self, db, collection, update_command, query_document=None, is_upsert=True):
        mongo_update_command = {"$set": update_command}
        result = self._client[db][collection].update_many(query_document, mongo_update_command, is_upsert)
        return result.modified_count or result.upserted_id is not None

    def update_or_replace(self, db, collection, query, data):
        result = self._client[db][collection].update(query, data, upsert=True)
        return result

    def push(self, db, collection, query_document, field, data):
        mongo_data = {"$push": {field: data}}
        result = self._client[db][collection].update_many(query_document, mongo_data)
        return result.modified_count or result.upserted_id is not None

    def pop(self, db, collection, query_document, field):
        mongo_data = {"$pop": {field: 1}}
        result = self._client[db][collection].update_many(query_document, mongo_data)
        return result.modified_count or result.upserted_id is not None

    def delete(self, db, collection, query_document=None):
        return self._client[db][collection].delete_many(query_document)

    def mark_as_deleted(self, db, collection, id_to_mark):
        query_document = {'id': id_to_mark}
        update_command = {"$set": {"is_deleted": True}}
        result = self._client[db][collection].update_many(query_document, update_command)
        return result.modified_count or result.upserted_id is not None

    def delete_collection(self, db, collection):
        database = self._client[db]
        return database.drop_collection(collection)

    @staticmethod
    def _build_query_document(*query_documents):
        base_query_document = {
            "$or": [
                {"is_deleted": False},
                {"is_deleted": {"$exists": False}}
            ]
        }

        if len(query_documents) == 1 and query_documents[0] is None:
            return base_query_document
        else:
            and_condition = [base_query_document]
            for q in query_documents:
                if q is not None:
                    and_condition.append(q)
            return {
                "$and": and_condition
            }
