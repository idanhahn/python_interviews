from logging import getLogger

from be_common.enums.common import ENTITY_ID, PAYLOAD, PD_DIR_PD_LOCATION, PD_DIR_INCIDENT_LOCATION, PD_DIR_DIRECTIONS, \
    PD_DIR_PD_ASSIGN, PD_DIR_INCIDENT_ID
from be_common.utils.misc import utc_now
from be_mongo_adapter.data_access.schema_conversions.base_schema import BaseSchema
from be_mongo_adapter.data_access.schema_conversions.conversion_helpers import build_coordinate_point_to_mongo, \
    build_location_to_application_other_field

log = getLogger(__name__)


class PDDirectionToIncidentSchema(BaseSchema):
    @staticmethod
    def to_mongodb(data):
        log.debug("convert message to mongodb format, application entity: {}".format(data))
        entity = data
        return {
            'id': entity.get(ENTITY_ID),
            'last_update': utc_now(),
            'incident_id': entity.get(PD_DIR_INCIDENT_ID, None),
            'incident_location': build_coordinate_point_to_mongo(**entity.get(PD_DIR_INCIDENT_LOCATION)),
            'pd_location': build_coordinate_point_to_mongo(**entity.get(PD_DIR_PD_LOCATION)),
            'pd_id': entity.get(PD_DIR_PD_ASSIGN, None),
            'directions': entity.get(PD_DIR_DIRECTIONS, None),
        }

    @staticmethod
    def to_application(mongo_entity):
        log.debug("convert message to application format, mongo entity: {}".format(mongo_entity))
        return {
            ENTITY_ID: mongo_entity.get('id'),
            PD_DIR_INCIDENT_ID: mongo_entity.get('incident_id'),
            PD_DIR_PD_ASSIGN: mongo_entity.get('pd_id'),
            PD_DIR_DIRECTIONS: mongo_entity.get('directions'),
            PD_DIR_INCIDENT_LOCATION: build_location_to_application_other_field(mongo_entity, 'incident_location'),
            PD_DIR_PD_LOCATION: build_location_to_application_other_field(mongo_entity, 'pd_location'),
        }
