from logging import getLogger

from be_common.enums.common import LOCATION, ENTITY_ID, CREATION_TIME, TYPE, SUBTYPE, \
    PAYLOAD, IS_DELETED, IS_ASSIGNED, USER_ASSIGNED, SECTION, I_BASED_ON, ID_IN_SOURCE, SOURCE, I_TIME, I_REPORT_TYPE, \
    I_USER_ID, I_CAMERA_FEED, RAW, RELIABILITY, CONFIDENCE, DETECTION, TIME, UI_SPILLMAN_INFORMATION, INCIDENT_STATE, \
    WAYCARE_SYSTEM, EVENT_LOG, PATHS, I_REPORT_INFORMATION
from be_common.utils.misc import deep_get, utc_now
from be_mongo_adapter.data_access.schema_conversions.base_schema import BaseSchema
from be_mongo_adapter.data_access.schema_conversions.conversion_helpers import build_coordinate_point_to_mongo, \
    build_location_to_application

log = getLogger(__name__)


class IncidentSchema(BaseSchema):
    # todo: add source (FAST/PD) after definition
    @staticmethod
    def to_mongodb(data):
        log.debug("convert message to mongodb format, application entity: {}".format(data))
        entity = data[PAYLOAD]
        return {
            'id': entity.get(ENTITY_ID),
            'creation_time': data[CREATION_TIME],
            'location': build_coordinate_point_to_mongo(**entity.get(LOCATION)),
            'section': entity.get(SECTION),
            'type': entity.get(TYPE),
            'subtype': entity.get(SUBTYPE),
            'is_assigned': entity.get(IS_ASSIGNED, False),
            'user_assigned': entity.get(USER_ASSIGNED, None),
            'is_deleted': entity.get(IS_DELETED, False),
            'based_on': {
                'id_in_source': deep_get(data[PAYLOAD], I_BASED_ON, ID_IN_SOURCE),
                'source': deep_get(data[PAYLOAD], I_BASED_ON, SOURCE),
            },
            'time': entity.get(I_TIME),
            'camera_feed': entity.get(I_CAMERA_FEED),
            'user_id': entity.get(I_USER_ID, WAYCARE_SYSTEM),
            'report_type': entity.get(I_REPORT_TYPE),
            'last_update': utc_now(),            
            'source': entity.get(SOURCE),
            'raw': data[RAW],
            'reliability': entity.get(RELIABILITY),
            'confidence': entity.get(CONFIDENCE),
            'id_in_source': entity.get(ID_IN_SOURCE),
            'detection': entity.get(DETECTION),
            'incident_state': entity.get(INCIDENT_STATE),
            'spillman_information': entity.get(UI_SPILLMAN_INFORMATION),
            'report_information': entity.get(I_REPORT_INFORMATION),
            'paths': entity.get(PATHS),
        }

    @staticmethod
    def to_application(mongo_entity):
        log.debug("convert message to application format, mongo entity: {}".format(mongo_entity))
        return {
            ENTITY_ID: mongo_entity.get('id'),
            CREATION_TIME: mongo_entity.get('creation_time'),
            LOCATION: build_location_to_application(mongo_entity),
            SECTION: mongo_entity.get('section'),
            TYPE: mongo_entity.get('type'),
            SUBTYPE: mongo_entity.get('subtype'),
            IS_DELETED: mongo_entity.get('is_deleted'),
            IS_ASSIGNED: mongo_entity.get('is_assigned'),
            USER_ASSIGNED: mongo_entity.get('user_assigned'),
            I_BASED_ON: {
                ID_IN_SOURCE: deep_get(mongo_entity, 'based_on', 'id_in_source'),
                SOURCE: deep_get(mongo_entity, 'based_on', 'source'),
            },
            I_TIME: mongo_entity.get('time'),
            I_CAMERA_FEED: mongo_entity.get('camera_feed'),
            I_USER_ID: mongo_entity.get('user_id'),
            I_REPORT_TYPE: mongo_entity.get('report_type'),
            RAW: mongo_entity.get('raw'),
            RELIABILITY: mongo_entity.get('reliability'),
            CONFIDENCE: mongo_entity.get('confidence'),
            ID_IN_SOURCE: mongo_entity.get('id_in_source'),
            DETECTION: mongo_entity.get('detection'),
            SOURCE: mongo_entity.get('source'),
            TIME: mongo_entity.get('time'),
            UI_SPILLMAN_INFORMATION: mongo_entity.get('spillman_information'),
            INCIDENT_STATE: mongo_entity.get('incident_state'),
            EVENT_LOG: mongo_entity.get('event_log'),
            PATHS: mongo_entity.get('paths'),
            I_REPORT_INFORMATION: mongo_entity.get('report_information'),
        }
