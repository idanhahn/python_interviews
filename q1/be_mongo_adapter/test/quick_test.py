import unittest

from be_mongo_adapter.data_access.mongo_adapter.mongo_adapter import MongoAdapter


class MongoAdapterTest(unittest.TestCase):
    def setUp(self):
        self._mongo_adapter = MongoAdapter(host="localhost")
        self._mongo_adapter.delete_collection('test_db', 'test_collection')

    def tearDown(self):
        self._mongo_adapter.close()
'''
    def test_insert_single_entity(self):
        self._mongo_adapter.insert('test_db', 'test_collection', {'key': 'value1'})
'''

'''
    def test_insert_many(self):
        
        self._mongo_adapter.insert('test_db', 'test_collection', {'key': 'value1'})

        self._mongo_adapter.insert('test_db', 'test_collection', [
            {'key': 'value2'},
            {'key': 'value3'},
            {'key': 'value4'}
        ])
'''

'''
    def test_update(self):

        self._mongo_adapter.update(
            db='test_db',
            collection='test_collection',
            documents={
                'id': '1',
                'key': 'value1',
        })

        self._mongo_adapter.update(
         db='test_db',
         collection='test_collection',
         documents={
                    'id': '1',
                    'key': 'value2',
        })
'''


'''
    def test_update_many(self):

        result = self._mongo_controller.update('test_db', 'test_collection', [
            {'key': 'value1'},
            {'key': 'value2'},
            {'other_key': 'value3'}
        ])
'''

if __name__ == '__main__':
    unittest.main()
