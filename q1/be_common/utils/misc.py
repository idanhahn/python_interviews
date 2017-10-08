from datetime import datetime, timedelta
import re
from functools import reduce

import pytz

from be_dexter_service.definitions.common_dexter_extension import Ptr


def merge_two_dicts(x, y):
    """
    Given two dicts, merge them into a new dict as a shallow copy.
    """
    z = x.copy()
    z.update(y)
    return z


def round_time(dt=None, round_to=60):
    """
    Round a datetime object to any time laps in seconds

    :param dt: datetime.datetime object, default now.
    :param round_to: Closest number of seconds to round to, default 1 minute.
    """
    if dt is None:
        dt = datetime.utcnow()
    seconds = (dt.replace(tzinfo=None) - dt.min).seconds
    rounding = (seconds + round_to / 2) // round_to * round_to
    return dt + timedelta(0, rounding - seconds, -dt.microsecond)


def convert_to_camel_case(snake_case):
    first, *rest = snake_case.split('_')
    return first + ''.join(word.capitalize() for word in rest)

first_cap_re = re.compile('(.)([A-Z][a-z]+)')
all_cap_re = re.compile('([a-z0-9])([A-Z])')


def convert_to_snake_case(name):
    s1 = first_cap_re.sub(r'\1_\2', name)
    return all_cap_re.sub(r'\1_\2', s1).lower()


def convert_ptr_type_to_enum_type(item):
    return convert_to_snake_case(item[Ptr.TYPE.value]).upper()


def utc_now():
    return datetime.utcnow().replace(tzinfo=pytz.utc)


def utcfromtimestamp(timestamp):
    return datetime.utcfromtimestamp(timestamp).replace(tzinfo=pytz.utc)


def js_to_py_timestamp(js_timestamp):
    return js_timestamp / 1000


def py_to_js_timestamp(py_timestamp):
    return int(py_timestamp * 1000)


def pairwise(iterable):
    it = iter(iterable)
    a = next(it, None)

    for b in it:
        yield (a, b)
        a = b


def deep_get(dictionary, *keys, default=None):
    # deep_get(my_dict, key1, key2) == my_dict[key1][key2]
    val = reduce(lambda d, key: d.get(key) if d else None, keys, dictionary)
    return default if val is None else val
