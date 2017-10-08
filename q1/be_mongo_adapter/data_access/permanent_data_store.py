from logging import getLogger

from be_common.enums.common import LOCATION, WAYCARE_SYSTEM, EntityType, USER_NAME, PATH
from be_mongo_adapter.data_access.mongo_adapter import mongo_adapter_instance
from be_mongo_adapter.data_access.schema_conversions.camera_schema import CameraSchema
from be_mongo_adapter.data_access.schema_conversions.conversion_helpers import build_coordinate_point_to_mongo, \
    build_path_coordinate_to_mongo
from be_mongo_adapter.data_access.schema_conversions.dms_schema import DmsSchema
from be_mongo_adapter.data_access.schema_conversions.incident_schema import IncidentSchema
from be_mongo_adapter.data_access.schema_conversions.milepost_schema import MilepostSchema
from be_mongo_adapter.data_access.schema_conversions.operator_schema import PoliceSchema
from be_mongo_adapter.data_access.schema_conversions.pd_direction_to_incident_schema import \
    PDDirectionToIncidentSchema
from be_mongo_adapter.data_access.schema_conversions.section_schema import SectionSchema
from be_mongo_adapter.data_access.schema_conversions.segment_schema import SegmentSchema

log = getLogger(__name__)


class PermanentDataStore:
    def __init__(self, cfg=None) -> None:
        super().__init__()
        if cfg is None:
            cfg = {"host": None, "db": 'waycare_db'}
        self._cfg = cfg
        self._logger = getLogger(__name__)
        self._conn = mongo_adapter_instance.get_client(host=cfg["host"])

    def is_exist_by_id(self, entity_type, entity_id, unfiltered=False):
        results = self.find(
            entity_type=entity_type,
            query_document={'id': entity_id},
            unfiltered=unfiltered
        )

        if not results:
            return False
        return True

    def is_exist_by_query(self, entity_type, query, unfiltered=False):
        result = self.find(
            entity_type=entity_type,
            query_document=query,
            unfiltered=unfiltered,
        )

    def find(self, entity_type, query_document=None, unfiltered=False):
        results = self._conn.find(
            self._cfg["db"],
            PermanentDataStore._get_collection(entity_type),
            query_document,
            unfiltered
        )

        return self._convert_data_to_application(results, entity_type)

    def find_one(self, entity_type, query_document=None, unfiltered=False):
        results = self._conn.find_one(
            db=self._cfg["db"],
            collection=PermanentDataStore._get_collection(entity_type),
            original_query_document=query_document,
            unfiltered=unfiltered
        )

        if not results:
            return None

        results = self._convert_data_to_application([results], entity_type)
        return results[0]

    def find_near_by(self, entity_type, location, location_attr=LOCATION, additional_query=None, max_distance=1000):
        results = self._conn.find_by_distance(
            db=self._cfg["db"],
            collection=PermanentDataStore._get_collection(entity_type),
            location=build_coordinate_point_to_mongo(**location),
            location_field_name=location_attr,
            max_distance=max_distance,
            additional_query=additional_query
        )

        return self._convert_data_to_application(results, entity_type)

    def save(self, entity_type, data):
        collection, model = self._convert_data_to_adapter(entity_type, data)

        return self._conn.insert(self._cfg["db"], collection, model)

    def save_or_update_by_query(self, entity_type, query, data):
        collection, model = self._convert_data_to_adapter(entity_type, data)
        return self._conn.update_or_replace(
            db=self._cfg["db"],
            collection=collection,
            query=query,
            data=model,
        )

    def get_user_name(self, user_id):
        if user_id == WAYCARE_SYSTEM:
            return WAYCARE_SYSTEM

        user = self.find_one(
            entity_type=EntityType.OPERATOR.value,
            query_document={"user_id": user_id},
            unfiltered=True
        )
        user_name = user.get(USER_NAME, None)
        if user_name is None:
            user = self.find_one(
                entity_type=EntityType.POLICE.value,
                query_document={"user_id": user_id},
                unfiltered=True
            )
            user_name = user.get(USER_NAME, None)

            if user_name is None:
                user_name = user_id

        return user_name

    def update_by_filter(self, entity_type, filter_dict, update_fields_dict):
        if LOCATION in update_fields_dict:
            update_fields_dict[LOCATION] = build_coordinate_point_to_mongo(**update_fields_dict[LOCATION])
        elif PATH in update_fields_dict:
            update_fields_dict[PATH] = build_path_coordinate_to_mongo(update_fields_dict[PATH])

        return self._conn.update(
            self._cfg["db"],
            PermanentDataStore._get_collection(entity_type),
            update_fields_dict,
            filter_dict,
        )

    def soft_delete(self, entity_type, id_to_delete):
        log.info("going to perform soft delete. entity type: {}, id: {}".format(entity_type, id_to_delete))
        return self._conn.mark_as_deleted(
            self._cfg["db"],
            PermanentDataStore._get_collection(entity_type),
            id_to_delete,
        )

    def push(self, entity_type, query, field, data):
        return self._conn.push(
            self._cfg["db"],
            PermanentDataStore._get_collection(entity_type),
            query,
            field,
            data,
        )

    def pop(self, entity_type, query, field):
        return self._conn.pop(
            self._cfg["db"],
            PermanentDataStore._get_collection(entity_type),
            query,
            field
        )

    @staticmethod
    def _convert_data_to_application(results, data_type):
        if data_type == EntityType.INCIDENT.value:
            formatted_results = map(IncidentSchema.to_application, results)
        elif data_type == EntityType.CAMERA.value:
            formatted_results = map(CameraSchema.to_application, results)
        elif data_type == EntityType.SECTION.value:
            formatted_results = map(SectionSchema.to_application, results)
        elif data_type == EntityType.SEGMENT.value:
            formatted_results = map(SegmentSchema.to_application, results)
        elif data_type == EntityType.DMS.value:
            formatted_results = map(DmsSchema.to_application, results)
        elif data_type == EntityType.POLICE.value:
            formatted_results = map(PoliceSchema.to_application, results)
        elif data_type == EntityType.HIGHWAY_MILEPOST.value:
            formatted_results = map(MilepostSchema.to_application, results)
        elif data_type == EntityType.PD_DIRECTION_TO_INCIDENT.value:
            formatted_results = map(PDDirectionToIncidentSchema.to_application, results)
        # todo: change the schema
        elif data_type == EntityType.INFRASTRUCTURE.value:
            formatted_results = map(IncidentSchema.to_application, results)
        # todo: change the schema
        elif data_type == EntityType.CONSTRUCTION.value:
            formatted_results = map(IncidentSchema.to_application, results)
        # todo: change the schema
        elif data_type == EntityType.EVENT.value:
            formatted_results = map(IncidentSchema.to_application, results)
        else:
            formatted_results = results
        return list(formatted_results)

    @staticmethod
    def _convert_data_to_adapter(data_type, data):
        if data_type == EntityType.INCIDENT.value:
            permanent_data = IncidentSchema.to_mongodb(data)
        # todo: change the schema
        elif data_type == EntityType.INFRASTRUCTURE.value:
            permanent_data = IncidentSchema.to_mongodb(data)
        # todo: change the schema
        elif data_type == EntityType.EVENT.value:
            permanent_data = IncidentSchema.to_mongodb(data)
        # todo: change the schema
        elif data_type == EntityType.CONSTRUCTION.value:
            permanent_data = IncidentSchema.to_mongodb(data)
        elif data_type == EntityType.POLICE.value:
            permanent_data = PoliceSchema.to_mongodb(data)
        elif data_type == EntityType.PD_DIRECTION_TO_INCIDENT.value:
            permanent_data = PDDirectionToIncidentSchema.to_mongodb(data)
        else:
            permanent_data = data
        return PermanentDataStore._get_collection(data_type), permanent_data

    @staticmethod
    def _get_collection(data_type):
        return "{}s".format(data_type)
