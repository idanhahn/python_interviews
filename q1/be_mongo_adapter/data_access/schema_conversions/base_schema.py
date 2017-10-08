import abc
from logging import getLogger

log = getLogger(__name__)


class BaseSchema(metaclass=abc.ABCMeta):

    @staticmethod
    @abc.abstractmethod
    def to_mongodb(data):
        pass

    @staticmethod
    @abc.abstractclassmethod
    def to_application(mongo_entity):
        pass
