from logging import getLogger

from be_common.enums.common import LOCATION, ENTITY_ID, CREATION_TIME, TYPE, SUBTYPE, SOURCE, \
    PAYLOAD, IS_DELETED, RAW, RELIABILITY, CONFIDENCE, ID_IN_SOURCE, DETECTION, UI_PD_SQUAD, \
    UI_STATUS, UI_SPILLMAN_CONTACT_NAME, TIME, IS_ASSIGNED, USER_ASSIGNED, SECTION, \
    UI_SPILLMAN_CONTACT, UI_CITY_CODE, UI_SPILLMAN_INFORMATION
from be_common.enums.incident_attributes import IncidentSource
from be_common.utils.misc import utc_now
from be_mongo_adapter.data_access.schema_conversions.base_schema import BaseSchema
from be_mongo_adapter.data_access.schema_conversions.conversion_helpers import build_coordinate_point_to_mongo, \
    build_location_to_application

log = getLogger(__name__)


class UnconfirmedIncidentSchema(BaseSchema):
    @staticmethod
    # todo: save and restore event time
    def to_mongodb(data):
        log.debug("convert message to mongo format, entity: {}".format(data))
        database_entity = {
            'id': data[PAYLOAD][ENTITY_ID],
            'creation_time': data[CREATION_TIME],
            'location': build_coordinate_point_to_mongo(**data[PAYLOAD][LOCATION]),
            'section': data[PAYLOAD][SECTION],
            'type': data[PAYLOAD][TYPE],
            'subtype': data[PAYLOAD][SUBTYPE],
            'time': data[PAYLOAD][TIME],
            'source': data[PAYLOAD][SOURCE],
            'raw': data[RAW],
            'reliability': data[PAYLOAD][RELIABILITY],
            'confidence': data[PAYLOAD][CONFIDENCE],
            'id_in_source': data[PAYLOAD][ID_IN_SOURCE],
            'detection': data[PAYLOAD][DETECTION],
            'last_update': utc_now(),
            'is_deleted': False,
            'is_assigned': False,
            'user_assigned': None,
        }

        if data[PAYLOAD][SOURCE] == IncidentSource.SPILLMAN_INCIDENT.value:
            database_entity['spillman_information'] = data[PAYLOAD][UI_SPILLMAN_INFORMATION]
        return database_entity

    @staticmethod
    def to_application(mongo_entity):
        log.debug("convert message to application format, mongo entity: {}".format(mongo_entity))
        return {
            ENTITY_ID: mongo_entity['id'],
            CREATION_TIME: mongo_entity['creation_time'],
            LOCATION: build_location_to_application(mongo_entity),
            SECTION: mongo_entity['section'],
            TYPE: mongo_entity['type'],
            SUBTYPE: mongo_entity['subtype'],
            RAW: mongo_entity['raw'],
            RELIABILITY: mongo_entity['reliability'],
            CONFIDENCE: mongo_entity['confidence'],
            ID_IN_SOURCE: mongo_entity['id_in_source'],
            DETECTION: mongo_entity['detection'],
            SOURCE: mongo_entity['source'],
            TIME: mongo_entity['time'],
            IS_DELETED: mongo_entity['is_deleted'],
            IS_ASSIGNED: mongo_entity['is_assigned'],
            USER_ASSIGNED: mongo_entity['user_assigned'],
            UI_SPILLMAN_INFORMATION: mongo_entity.get('spillman_information'),
        }
