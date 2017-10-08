from logging import getLogger

from be_common.enums.common import ENTITY_ID, LOCATION, DMS_CURRENT_MESSAGE, DMS_LAST_USER, \
    DMS_LAST_UPDATE, DMS_STATUS, DMS_NEW_MESSAGE, DMS_RAW_MESSAGE, ENTITY_TYPE, EntityType
from be_mongo_adapter.data_access.schema_conversions.base_schema import BaseSchema
from be_mongo_adapter.data_access.schema_conversions.conversion_helpers import build_location_to_application

log = getLogger(__name__)


class DmsSchema(BaseSchema):
    @staticmethod
    def to_mongodb(data):
        pass

    @staticmethod
    def to_application(mongo_entity):
        log.debug("convert message to application format, mongo entity: {}".format(mongo_entity))
        return {
            ENTITY_ID: mongo_entity['id'],
            LOCATION: build_location_to_application(mongo_entity),
            DMS_CURRENT_MESSAGE: mongo_entity['message'],
            DMS_RAW_MESSAGE: mongo_entity['raw_message'],
            DMS_NEW_MESSAGE: mongo_entity['new_message'],
            DMS_LAST_UPDATE: mongo_entity['last_update'],
            DMS_LAST_USER: mongo_entity['last_user'],
            DMS_STATUS: mongo_entity['status'],
            ENTITY_TYPE: EntityType.DMS.value,
            #todo: support direction, title etc'
            'title': mongo_entity['title'],
            'direction': mongo_entity['direction'],
            'travel_time': mongo_entity['travel_time'],
        }
