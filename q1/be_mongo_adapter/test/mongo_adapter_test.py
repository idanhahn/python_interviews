import unittest

from be_mongo_adapter.data_access.mongo_adapter.mongo_adapter import MongoAdapter


class MongoAdapterTest(unittest.TestCase):
    def setUp(self):
        self._mongo_controller = MongoAdapter(host="localhost")
        self._mongo_controller.delete_collection('test_db', 'test_collection')

    def tearDown(self):
        self._mongo_controller.close()

    def test_insert_single_entity(self):
        result = self._mongo_controller.insert('test_db', 'test_collection', {'key': 'value1'})
        self.assertTrue('_id' in result)
        self.assertIsInstance(result['_id'], str)

    def test_insert_many_entities(self):
        doc1 = {'key': 'value1'}
        doc2 = {'key': 'value1'}
        doc3 = {'key': 'value1'}

        results = self._mongo_controller.insert('test_db', 'test_collection', doc1, doc2, doc3)
        self.assertTrue(len(results) == 3)
        for result in results:
            self.assertTrue('_id' in result)
            self.assertIsInstance(result['_id'], str)

        docs = [{'key': 'value1'}, {'key': 'value1'}, {'key': 'value1'},
                {'key': 'value1'}, {'key': 'value1'}, {'key': 'value1'}]
        results = self._mongo_controller.insert('test_db', 'test_collection', docs)
        self.assertTrue(len(results) == 6)
        for result in results:
            self.assertTrue('_id' in result)
            self.assertIsInstance(result['_id'], str)

    def test_find_one_return_none(self):
        results = self._mongo_controller.find_one('test_db', 'test_collection')
        self.assertFalse(results)

    def test_find_one_without_query(self):
        docs = [{'key': 'value1'}, {'key': 'value1'}, {'key': 'value1'},
                {'key': 'value1'}, {'key': 'value1'}, {'key': 'value1'}]
        insert_results = self._mongo_controller.insert('test_db', 'test_collection', docs)

        results = self._mongo_controller.find_one('test_db', 'test_collection')
        self.assertIsInstance(results, dict)
        self.assertTrue('_id' in results)
        self.assertIsInstance(results['_id'], str)

    def test_find_one_with_query(self):
        docs = [{'key': 'value1'}, {'key': 'value1'}, {'key': 'value1'},
                {'key': 'value1'}, {'key': 'value1'}, {'key': 'value1'}]
        insert_results = self._mongo_controller.insert('test_db', 'test_collection', docs)

        results = self._mongo_controller.find_one('test_db', 'test_collection', {"key": "value1"})
        self.assertIsInstance(results, dict)
        self.assertTrue('_id' in results)
        self.assertIsInstance(results['_id'], str)

    def test_find_return_none(self):
        results = self._mongo_controller.find('test_db', 'test_collection')
        self.assertTrue(len(results) == 0)
        self.assertFalse(results)

    def test_find_without_query(self):
        docs = [{'key': 'value1'}, {'key': 'value1'}, {'key': 'value1'},
                {'key': 'value1'}, {'key': 'value1'}, {'key': 'value1'}]
        insert_results = self._mongo_controller.insert('test_db', 'test_collection', docs)

        results = self._mongo_controller.find('test_db', 'test_collection')
        self.assertTrue(len(results) == 6)
        for result in results:
            self.assertTrue('_id' in result)
            self.assertIsInstance(result['_id'], str)

    def test_find_with_query(self):
        docs = [{'key': 'value1'}, {'key': 'value1'}, {'key': 'value1'},
                {'key': 'value1'}, {'key': 'value1'}, {'key': 'value1'}]
        insert_results = self._mongo_controller.insert('test_db', 'test_collection', docs)

        results = self._mongo_controller.find('test_db', 'test_collection', {"key": "value1"})
        self.assertTrue(len(results) == 6)
        for result in results:
            self.assertTrue('_id' in result)
            self.assertIsInstance(result['_id'], str)

if __name__ == '__main__':
    unittest.main()
