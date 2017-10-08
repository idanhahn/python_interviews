from logging import getLogger

from be_common.enums.common import LOCATION, ENTITY_ID, CREATION_TIME, PAYLOAD, PD_USER_ID, TIME, \
    PD_TASK_ID, PD_STATE, \
    PD_USER_NAME, PD_TASK_TYPE, EMAIL
from be_mongo_adapter.data_access.schema_conversions.base_schema import BaseSchema
from be_mongo_adapter.data_access.schema_conversions.conversion_helpers import build_coordinate_point_to_mongo, \
    build_location_to_application

log = getLogger(__name__)

class PoliceSchema(BaseSchema):
    # todo: add source (FAST/PD) after definition
    @staticmethod
    def to_mongodb(data):
        return {
            'id': data[PAYLOAD][ENTITY_ID],
            'creation_time': data[CREATION_TIME],
            'user_id': data[PAYLOAD][PD_USER_ID],
            'location': build_coordinate_point_to_mongo(**data[PAYLOAD][LOCATION]),
            'last_update': data[PAYLOAD][TIME],
            'state': data[PAYLOAD][PD_STATE],
            'task_id': data[PAYLOAD][PD_TASK_ID],
            'task_type': data[PAYLOAD][PD_TASK_TYPE],
        }

    @staticmethod
    def to_application(mongo_entity):
        log.debug("convert message to application format, mongo entity: {}".format(mongo_entity))
        return {
            ENTITY_ID: mongo_entity['id'],
            PD_USER_ID: mongo_entity['user_id'],
            PD_USER_NAME: mongo_entity['user_name'],
            LOCATION: build_location_to_application(mongo_entity),
            TIME: mongo_entity['last_update'],
            PD_STATE: mongo_entity['state'],
            PD_TASK_ID: mongo_entity['task_id'],
            PD_TASK_TYPE: mongo_entity['task_type'],
            EMAIL: mongo_entity['email'],
        }
