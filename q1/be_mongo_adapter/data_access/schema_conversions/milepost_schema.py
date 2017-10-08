from logging import getLogger

from be_common.enums.common import LOCATION, ENTITY_ID, PATH, MP_MILEPOST, MP_DIRECTION, \
    MP_ROAD_NAME
from be_mongo_adapter.data_access.schema_conversions.base_schema import BaseSchema
from be_mongo_adapter.data_access.schema_conversions.conversion_helpers import build_location_to_application, \
    build_path_to_application

log = getLogger(__name__)


class MilepostSchema(BaseSchema):
    @staticmethod
    # todo: save and restore event time
    def to_mongodb(data):
        pass

    @staticmethod
    def to_application(mongo_entity):
        log.debug("convert message to application format, mongo entity: {}".format(mongo_entity))
        return {
            ENTITY_ID: mongo_entity[ENTITY_ID],
            MP_ROAD_NAME: mongo_entity['road_name'],
            MP_MILEPOST: mongo_entity['milepost'],
            MP_DIRECTION: mongo_entity['direction'],
            LOCATION: build_location_to_application(mongo_entity),
            PATH: build_path_to_application(mongo_entity),
        }


