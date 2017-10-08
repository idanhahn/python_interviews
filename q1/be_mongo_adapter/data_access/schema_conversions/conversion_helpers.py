from be_common.enums.common import LOCATION, LNG, LAT, PATH

COORDINATES = 'coordinates'


def build_coordinate_point_to_mongo(lat=0, lng=0):
    return {
        'type': "Point",
        COORDINATES: [lng, lat]
    }


def build_path_coordinate_to_mongo(path):
    if path is None or not path:
        return {}
    _path = [[point['lng'], point['lat']] for point in path]
    return {
        'type': "LineString",
        COORDINATES: _path
    }


def build_location_to_application(mongo_entity):
    lng, lat = mongo_entity[LOCATION][COORDINATES]
    return {LAT: lat, LNG: lng}


def build_location_to_application_other_field(mongo_entity, field_name):
    lng, lat = mongo_entity[field_name][COORDINATES]
    return {LAT: lat, LNG: lng}


def build_path_to_application(mongo_entity):
    return [{LAT: lat, LNG: lng} for lng, lat in mongo_entity[PATH][COORDINATES]]

def build_location_from_path_to_application(mongo_entity):
    lng, lat = mongo_entity[PATH][COORDINATES][int(len(mongo_entity[PATH][COORDINATES])/2)]
    return {LAT: lat, LNG: lng}
