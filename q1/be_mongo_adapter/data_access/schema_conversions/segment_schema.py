from logging import getLogger

from be_common.enums.common import ENTITY_ID, PATH, ROAD_NUMBER, ROAD_TYPE, STREET, SECTIONS, \
    LOCATION, IS_ASSIGNED, USER_ASSIGNED, CURRENT_PREDICTION
from be_mongo_adapter.data_access.schema_conversions.base_schema import BaseSchema
from be_mongo_adapter.data_access.schema_conversions.conversion_helpers import build_path_to_application, \
    build_location_from_path_to_application

log = getLogger(__name__)


class SegmentSchema(BaseSchema):
    @staticmethod
    def to_mongodb(data):
        pass

    @staticmethod
    def to_application(mongo_entity):
        log.debug("convert message to application format, mongo entity: {}".format(mongo_entity))
        return {
            ENTITY_ID: mongo_entity['id'],
            PATH: build_path_to_application(mongo_entity),
            ROAD_TYPE: mongo_entity['road_type'],
            ROAD_NUMBER: mongo_entity['road_number'],
            STREET: mongo_entity['street'],
            SECTIONS: mongo_entity['sections'],
            LOCATION: build_location_from_path_to_application(mongo_entity),
            IS_ASSIGNED: mongo_entity['is_assigned'],
            USER_ASSIGNED: mongo_entity['user_assigned'],
            CURRENT_PREDICTION: mongo_entity['current_prediction']
        }
