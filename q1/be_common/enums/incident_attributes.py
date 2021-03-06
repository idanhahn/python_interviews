from enum import Enum


#################################################
# secondary fields for UNCONFIRMED_INCIDENT
# with source WAZE_TRAFFIC_ALERT
#################################################

class IncidentSource(Enum):
    """
    Unconfirmed incident data sources that are appended to msg
    """

    WAZE_TRAFFIC_ALERT = 'waze_traffic_alert'
    WAZE_TRAFFIC_JAM = 'waze_traffic_jam'
    WAZE_TRAFFIC_IRREGULARITIES = 'waze_traffic_irregularities'
    SPILLMAN_INCIDENT = 'spillman_incident'
    USER_INPUT = 'user_input'


class IncidentType(Enum):
    """
    All the possible incident types
    """
    CRASH = 'crash'
    HAZARD = 'hazard'
    SPECIAL_EVENT = 'special_event'  # 'crowd'
    INFRASTRUCTURE = 'infrastructure'
    CONSTRUCTION = 'construction'

    # client:
    # 'crash'
    # 'event',          'crowd'
    # 'infrastructure', 'trafficlight'
    # 'construction'
    # 'power-outage'
    # 'incident',       'unknown'


    # WAZE:
    # JAM = 'JAM'
    # HAZARD = 'HAZARD'
    # WEATHERHAZARD = 'WEATHERHAZARD'
    # MISC = 'MISC'
    # CONSTRUCTION = 'CONSTRUCTION'
    # ROAD_CLOSED = 'ROAD_CLOSED'


class IncidentSubType(Enum):
    """
    All the possible incident subtypes
    """
    # ACCIDENT
    MAJOR = 'major'
    MINOR = 'minor'
    EMPTY = ''

    # ACCIDENT
    ACCIDENT_MAJOR = 'ACCIDENT_MAJOR'
    ACCIDENT_MINOR = 'ACCIDENT_MINOR'
    ACCIDENT_EMPTY = ''

    # JAM
    JAM_MODERATE_TRAFFIC = 'JAM_MODERATE_TRAFFIC'
    JAM_HEAVY_TRAFFIC = 'JAM_HEAVY_TRAFFIC'
    JAM_STAND_STILL_TRAFFIC = 'JAM_STAND_STILL_TRAFFIC'
    JAM_LIGHT_TRAFFIC = 'JAM_STAND_STILL_TRAFFIC'
    JAM_EMPTY = ''

    # WEATHERHAZARD/HAZARD
    HAZARD_ON_ROAD = 'HAZARD_ON_ROAD'
    HAZARD_ON_SHOULDER = 'HAZARD_ON_SHOULDER'
    HAZARD_WEATHER = 'HAZARD_WEATHER'
    HAZARD_ON_ROAD_OBJECT = 'HAZARD_ON_ROAD_OBJECT'
    HAZARD_ON_ROAD_POT_HOLE = 'HAZARD_ON_ROAD_POT_HOLE'
    HAZARD_ON_ROAD_ROAD_KILL = 'HAZARD_ON_ROAD_ROAD_KILL'
    HAZARD_ON_SHOULDER_CAR_STOPPED = 'HAZARD_ON_SHOULDER_CAR_STOPPED'
    HAZARD_ON_SHOULDER_ANIMALS = 'HAZARD_ON_SHOULDER_ANIMALS'
    HAZARD_ON_SHOULDER_MISSING_SIGN = 'HAZARD_ON_SHOULDER_MISSING_SIGN'
    HAZARD_WEATHER_FOG = 'HAZARD_WEATHER_FOG'
    HAZARD_WEATHER_HAIL = 'HAZARD_WEATHER_HAIL'
    HAZARD_WEATHER_HEAVY_RAIN = 'HAZARD_WEATHER_HEAVY_RAIN'
    HAZARD_WEATHER_HEAVY_SNOW = 'HAZARD_WEATHER_HEAVY_SNOW'
    HAZARD_WEATHER_FLOOD = 'HAZARD_WEATHER_FLOOD'
    HAZARD_WEATHER_MONSOON = 'HAZARD_WEATHER_MONSOON'
    HAZARD_WEATHER_TORNADO = 'HAZARD_WEATHER_TORNADO'
    HAZARD_WEATHER_HEAT_WAVE = 'HAZARD_WEATHER_HEAT_WAVE'
    HAZARD_WEATHER_HURRICANE = 'HAZARD_WEATHER_HURRICANE'
    HAZARD_WEATHER_FREEZING_RAIN = 'HAZARD_WEATHER_FREEZING_RAIN'
    HAZARD_ON_ROAD_LANE_CLOSED = 'HAZARD_ON_ROAD_LANE_CLOSED'
    HAZARD_ON_ROAD_OIL = 'HAZARD_ON_ROAD_OIL'
    HAZARD_ON_ROAD_ICE = 'HAZARD_ON_ROAD_ICE'
    HAZARD_ON_ROAD_CONSTRUCTION = 'HAZARD_ON_ROAD_CONSTRUCTION'
    HAZARD_ON_ROAD_CAR_STOPPED = 'HAZARD_ON_ROAD_CAR_STOPPED'
    HAZARD_EMPTY = ''

    # MISC
    MISC_EMPTY = ''

    # DEFAULT
    DEFAULT = 'DEFAULT'

    # CONSTRUCTION
    CONSTRUCTION_EMPTY = ''

    # ROAD_CLOSED
    ROAD_CLOSED_HAZARD = 'ROAD_CLOSED_HAZARD'
    ROAD_CLOSED_CONSTRUCTION = 'ROAD_CLOSED_CONSTRUCTION'
    ROAD_CLOSED_EVENT = 'ROAD_CLOSED_EVENT'
    ROAD_CLOSED_EMPTY = ''

