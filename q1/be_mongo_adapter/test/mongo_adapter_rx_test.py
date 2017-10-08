from rx import Observer

from be_mongo_adapter.data_access.mongo_adapter.mongo_adapter import MongoAdapter


class MsgObserver(Observer):
    def on_next(self, value):
        print("Received {0}".format(value))

    def on_completed(self):
        print("Done!")

    def on_error(self, error):
        print("Error Occurred: {0}".format(error))


mongo_controller = MongoAdapter(host="172.17.0.2", port=27017)

# mongo_controller.insert('test_db', 'test_collection', {'key': 'value1'}) \
#     .subscribe(MsgObserver())
# mongo_controller.find_one('test_db', 'test_collection', {'key': 'value'}) \
#     .subscribe(MsgObserver())
# mongo_controller.find('test_db', 'test_collection') \
#     .subscribe(MsgObserver())

mongo_controller.find('test', 'cameras', {"location": {
    "$nearSphere": {"$geometry": {"type": "Point", "coordinates": [-115.1757, 36.1394]}, "$maxDistance": 1000}}})\
    .subscribe(MsgObserver())
