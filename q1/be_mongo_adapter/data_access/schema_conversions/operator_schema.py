from logging import getLogger

from be_common.enums.common import ENTITY_ID, PAYLOAD, TIME, \
    EMAIL, USER_NAME, USER_ID, PRIVILEGES, LAST_UPDATED
from be_mongo_adapter.data_access.schema_conversions.base_schema import BaseSchema

log = getLogger(__name__)

class PoliceSchema(BaseSchema):
    # todo: add source (FAST/PD) after definition
    @staticmethod
    def to_mongodb(data, USER_ID=None):
        return {
            'id': data[PAYLOAD][ENTITY_ID],
            'user_id': data[PAYLOAD][USER_ID],
            'last_update': data[PAYLOAD][TIME],
            'user_name': data[PAYLOAD][USER_NAME],
        }

    @staticmethod
    def to_application(mongo_entity):
        log.debug("convert message to application format, mongo entity: {}".format(mongo_entity))
        return {
            ENTITY_ID: mongo_entity['id'],
            USER_ID: mongo_entity['user_id'],
            USER_NAME: mongo_entity['user_name'],
            LAST_UPDATED: mongo_entity['last_update'],
            EMAIL: mongo_entity['email'],
            PRIVILEGES: mongo_entity['previleges'],
        }
