from enum import Enum

#########################################
# main fields that are always present
# except for PREDICTION entity_type
#########################################
FLOW_TYPE = 'flow_type'
ENTITY_TYPE = 'entity_type'
SYSID = 'sysid'
CREATION_TIME = 'creation_time'
PAYLOAD = 'payload'
RAW = 'raw'
_ID = '_id'
SUSPICIOUS = 'suspicious'


class FlowType(Enum):
    """
    Data types that are appended to each msg in Format Service
    """
    # Supported
    ADD_INCIDENT = 'add_incident'
    DELETE_INCIDENT = 'delete_incident'
    UNDO_DELETE_INCIDENT = 'undo_delete_incident'
    UPDATE_INCIDENT = 'update_incident'
    WEATHER_UPDATE = 'weather_update'
    WEATHER_FORECAST_UPDATE = 'weather_forecast_update'
    PD_LHB = 'pd_lhb'
    PD_EVENT = 'pd_event'
    HOURLY_PREDICTION = 'hourly_prediction'
    DMS = 'dms'
    CHANGE_DMS = 'change_dms'
    UPDATE_FSP_LOC = 'update_fsp_loc'

    # not implemented


class EntityType(Enum):
    INCIDENT = 'incident'
    SECTION = 'section'
    CAMERA = 'camera'
    SEGMENT = 'segment'
    WEATHER = 'weather'
    FORECAST = 'forecast'
    PD = 'pd'
    DMS = 'dms'
    HIGHWAY_MILEPOST = 'highway_milepost'
    PD_DIRECTION_TO_INCIDENT = 'pd_direction_to_incident'
    FSP_LOC = 'fsp_loc'

    # PREDICTION = 'prediction'

    # Not Supported
    FSP = 'fsp'
    EVENT = 'event'
    CONSTRUCTION = 'construction'
    INFRASTRUCTURE = 'infrastructure'
    POWER_OUTAGE = 'power_outage'
    POLICE = 'police'  # updates about police locations
    OPERATOR = 'operator'
    MDMS = 'mdms'  # updates about mdms location and text
    SPECIAL_DAY = 'special_day'
    JAM = 'jam'
    LIGHT_CONDITION = 'light_condition'
    SPECIAL_EVENT = 'special_event'
    EXHIBITION = 'exhibition'
    ROAD_DETECTOR = 'road_detector'
    IVB = 'ivb'


# GENERAL COMMON
ENTITY_ID = 'id'
TYPE = 'type'
SUBTYPE = 'subtype'
RELATED = 'related'
LOCATION = 'location'
TIME = 'time' #actual time (not system creation time)
PATH = 'path'
PATHS = 'paths'
SECTION = 'section'
SOURCE = 'source'
IS_DELETED = 'is_deleted'
IS_ASSIGNED = 'is_assigned'
USER_ASSIGNED = 'user_assigned'
CURRENT_PREDICTION = 'current_prediction'
USER_NAME = 'user_name'
CHANGE_DETECTIONS = 'change_detections'
WAYCARE_SYSTEM = 'waycare-system'
EMAIL = 'email'
USER_ID = 'user_id'
USER_NAME = 'user_name'
PRIVILEGES = 'privileges'
LAST_UPDATED = 'last_updated'

# GEO COMMONS
LAT = 'lat'
LNG = 'lng'

# Unconfirmed Incidents
DETECTION = 'detection' #if incident was confirmed as valid in incident detection algorithm : true
RELIABILITY = 'reliability'
CONFIDENCE = 'confidence'
ID_IN_SOURCE = 'id_in_source'


# Section
SUB_TITLE = 'sub_title'
STREET = 'street'
TITLE = 'title'
ROAD_TYPE = 'road_type'
ROAD_NUMBER = 'road_number'
SEGMENT = 'segment'
SEGMENT_ID = 'id'
SEGMENT_PATH = 'path'
NHP_SECTION_ID = 'nhp_section_id'
FAST_SECTION_ID = 'fast_section_id'
SECTION_ADDITIONAL_INFO = 'additional_info'
SECTION_PD_STREET_NAME = 'section_pd_street_name'
SECTION_PD_ADDITIONAL_INFO = 'section_pd_additional_info'
AUTO_GENERATED_SECTION = 'auto_generated_section'

# Mileposts
MP_ROAD_NAME = 'road_name'
MP_DIRECTION = 'direction'
MP_MILEPOST = 'milepost'

#todo: this is for segments schema (move to the right location in file)
SECTIONS = 'sections'


# FAST
# TODO: maybe merge fast & pd user ids
FAST_USER_ID = 'fast_user_id'


# Police Department
PD_USER_ID = 'pd_user_id'
PD_USER_NAME = 'pd_user_name'
PD_EVENT_TYPE = 'pd_event_type'
PD_TASK_ID = 'pd_task_id'
PD_TASK_TYPE = 'pd_task_type'
PD_AVAILABLE_TASKS = 'pd_available_tasks'
# sub types for lhb
PD_STATE = 'pd_state'
PD_ACTIVE_TASK_ID = 'pd_active_task_id'
PD_ACTIVE_TASK_TYPE = 'pd_active_task_type'
PD_ACTIVE_TASK_ROUTE = 'pd_active_task_route'
PD_ACTIVE_TASK_DIRECTION = 'pd_active_task_direction'

# Add Incident
I_REPORT_TYPE = 'report_type'
I_TYPE = 'type'
I_SUBTYPE = 'subtype'
I_TIME = 'time'
I_REASON = 'reason'
I_USER_ID = 'user_id'
I_CAMERA_FEED = 'camera_feed'
I_CONTACT = 'contact'
I_BASED_ON = 'based_on'
INCIDENT_STATE = 'incident_state'
EVENT_LOG = 'event_log'
CONFIRMED = 'confirmed'
UNCONFIRMED = 'unconfirmed'
I_LANES_BLOCKED = 'lanes_blocked'
I_LANES_NUMBER = 'lanes_number'
I_MEMO = 'memo'
I_CORRIDOR = 'corridor'
I_PLACE = 'place'
I_DESCRIPTION = 'description'
I_LEVEL = 'level'
I_IS_SECONDARY = 'is_secondary'
I_REPORT_INFORMATION = 'report_information'
I_REPORT_NEW_INCIDENT = 'new-incident'
I_REPORT_EDIT_INCIDENT = 'edit-incident'
I_REPORT_CONFIRMED_INCIDENT = 'from-unconfirmed-incident'
I_PREVIOUS_ENTITY_TYPE = 'previous_type'

# DMS
DMS_NEW_MESSAGE = 'new_message'
DMS_CURRENT_MESSAGE = 'current_message'
DMS_RAW_MESSAGE = 'raw_message'
DMS_USER_ID = 'user_id'
DMS_STATUS = 'status'
DMS_LAST_UPDATE = 'last_update'
DMS_LAST_USER = 'last_user'
    #FAST DMS
    #API_DMS

# Unconfirmed incident
UI_STATUS = 'status'
UI_PD_SQUAD = 'pd_squad'
UI_PD_ONLY = 'ui_pd_only'
UI_CITY_CODE = 'city_code'

# SPILLMAN
UI_SPILLMAN_INFORMATION = 'spillman_information'
UI_SPILLMAN_TYPE = 'spillman_type'
UI_SPILLMAN_SUB_FLOW = 'spillman_sub_type'
UI_SPILLMAN_CONTACT = 'contact'
UI_SPILLMAN_CONTACT_NAME = 'name'
UI_SPILLMAN_CONTACT_PHONE = 'tel'
UI_SPILLMAN_CALL_PRIORITY = 'spillman_priority'
UI_SPILLMAN_RESPOND_ADDRESS = 'response_address'
UI_SPILLMAN_STATUS = 'spillman_status'
UI_SPILLMAN_CITY_CODE = 'city_code'
UI_SPILLMAN_RESPONSIBLE_UNIT_NUMBER = 'responsible_unit_number'
UI_SPILLMAN_CALL_ZONE_CODE = 'call_zone_code'
UI_SPILMAN_LOCATION_EXIST = 'location_exist'


#FLATFORM ICONS
ICON_ACCIDENT = 'accident'
ICON_INCIDENT = 'incident'
ICON_CAMERA = 'video-camera'
ICON_UNKNOWN = 'incident'

# Camera
CAMERA_ENCODERTYPE = 'encodertype'
CAMERA_MULTICAST_ADDRESS = 'multicast_address'
CAMERA_ADDRESS = 'address'
CAMERA_CCTV_ID = 'cctv_id'

# Prediction
PREDICTION_TIME_SLOT_INTERVAL = 'time_slot_interval'
PREDICTION_SHIFTS = 'shifts'
PREDICTION_START_TIME = 'start_time'
PREDICTION_END_TIME = 'end_time'
PREDICTION_START_TIME_CAMEL_CASE = 'startTime'
PREDICTION_END_TIME_CAMEL_CASE = 'endTime'
PREDICTION_SEGMENTS = 'segments'
PREDICTION_SEGMENTS_ID = 'id'
PREDICTION_SEGMENTS_SCORE = 'score'

# PD_DIRECTION_TO_INCIDENT
PD_DIR_PD_LOCATION = 'pd_dir_pd_location'
PD_DIR_INCIDENT_LOCATION = 'pd_dir_incident_location'
PD_DIR_DIRECTIONS = 'pd_dir_directions'
PD_DIR_PD_ASSIGN = 'pd_dir_pd_assign'
PD_DIR_INCIDENT_ID = 'pd_dir_incident_id'

######################################################
# secondary fields for WEATHER & WEATHER FORECASTS
######################################################
STATION_LOCATION = 'location'
W_CONDITIONS = 'conditions'
TEMPERATURE = 'temperature'
VISIBILITY = 'visibility'
WIND = 'wind'
WIND_SPEED = 'wind_speed'
WIND_GUST = 'wind_gust'
WIND_DIRECTION = 'wind_direction'
RAIN = 'rain'
SNOW = 'snow'
FOG = 'fog'
HAIL = 'hail'
HUMIDITY = 'humidity'
W_FORECASTS = "forecasts"
W_FORECAST = "forecast"


# mandark types
class MandarkType(Enum):
    WAZE_TRAFFIC_ALERTS = 'waze_traffic_alerts_lv'
    SPILLMAN_ALERTS = 'road_incidents_nhp_live_lv'
    WEATHER = 'weather_underground_live_lv'
    WEATHER_FORECAST = 'weather_forecast_live_lv'
    DMS = 'dms_fast_live_lv'
    DMS_TT = 'dms_tt_fast_live_lv'
    FSP_LOC = 'geotab_fsp_location_live_lv'


# monkey types
class MonkeyType(Enum):
    ADD_INCIDENT = 'api_add_incident'
    DELETE_INCIDENT = 'api_delete_incident'
    UNDO_DELETE_INCIDENT = 'api_undo_delete_incident'
    PD_EVENT = 'api_pd_event'
    PD_LHB = 'api_pd_lhb'
    CHANGE_DMS = 'api_change_dms'


class PDEventType(Enum):
    # supported
    LOGGED_IN = 'logged-in'
    TASK_FINISHED = 'task-finished'
    TASK_ACCEPTED = 'task-accepted'
    TASK_DISCARDED = 'task-discarded'
    ARRIVED = 'arrived'
    DEPARTED = 'departed'

    # not implemented
    LOGGED_OUT = 'logged-out'


# FSP_LOC
FSP_BEARING = 'bearing'



