from logging import getLogger

from be_mongo_adapter.data_access.schema_conversions.base_schema import BaseSchema

log = getLogger(__name__)


class ForecastSchema(BaseSchema):
    @staticmethod
    def to_mongodb(data):
        pass

    @staticmethod
    def to_application(mongo_entity):
        pass
