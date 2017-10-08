from logging import getLogger

from be_common.enums.common import ENTITY_ID, PATH, ROAD_NUMBER, ROAD_TYPE, STREET, \
    FAST_SECTION_ID, NHP_SECTION_ID, SEGMENT, RELATED, TYPE
from be_mongo_adapter.data_access.schema_conversions.base_schema import BaseSchema
from be_mongo_adapter.data_access.schema_conversions.conversion_helpers import build_path_to_application

log = getLogger(__name__)


class SectionSchema(BaseSchema):
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
            FAST_SECTION_ID: mongo_entity['fast_section_id'],
            NHP_SECTION_ID: mongo_entity['nhp_section_id'],
            STREET: mongo_entity['street'],
            SEGMENT: {
                ENTITY_ID: mongo_entity['segment']['id']
            },
            RELATED: mongo_entity['related'],
            TYPE: mongo_entity['type']
        }
