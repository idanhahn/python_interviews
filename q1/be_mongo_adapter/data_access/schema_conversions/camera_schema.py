from logging import getLogger

from be_common.enums.common import ENTITY_ID, LOCATION, CAMERA_CCTV_ID, CAMERA_ADDRESS, \
    CAMERA_MULTICAST_ADDRESS, CAMERA_ENCODERTYPE, ENTITY_TYPE, EntityType
from be_mongo_adapter.data_access.schema_conversions.base_schema import BaseSchema
from be_mongo_adapter.data_access.schema_conversions.conversion_helpers import build_location_to_application

log = getLogger(__name__)


class CameraSchema(BaseSchema):
    @staticmethod
    def to_mongodb(data):
        pass

    @staticmethod
    def to_application(mongo_entity):
        log.debug("convert message to application format, mongo entity: {}".format(mongo_entity))
        return {
            ENTITY_ID: mongo_entity['id'],
            CAMERA_CCTV_ID: mongo_entity['CCTV_ID'],
            LOCATION: build_location_to_application(mongo_entity),
            CAMERA_ADDRESS: mongo_entity['ADDRESS'],
            CAMERA_MULTICAST_ADDRESS: mongo_entity['MULTICAST_ADDRESS'],
            CAMERA_ENCODERTYPE: mongo_entity['ENCODERTYPE'],
            ENTITY_TYPE: EntityType.CAMERA.value,
        }
