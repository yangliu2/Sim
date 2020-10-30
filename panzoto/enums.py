""" Set up enums to eliminate magic strings """

from enum import Enum, auto


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        """
        the value of the ENUM now become the lower case of the name
        :params: left because parent class has them
        """
        return name.lower()

class Names(AutoName):
    PANZOTO = auto()

class Gender(AutoName):
    FEMALE = auto()
    MALE = auto()

class Logging(AutoName):
    INFO = auto()
    WARNING = auto()
    DEBUG = auto()
    ERROR = auto()