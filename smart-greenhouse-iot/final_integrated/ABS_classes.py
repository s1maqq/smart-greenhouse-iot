import abc
import random


class Device(abc.ABC):
    def __init__(self, id, condition):
        self.id = id
        self.condition = condition

    @abc.abstractmethod
    def connect(self, *args):
        pass

    def get_id(self):
        return self.id

    def get_condition(self):
        return self.condition

    def set_id(self, new_id):
        self.id = new_id

    def set_condition(self, new_condition):
        self.condition = new_condition


class Sensor(abc.ABC):
    def __init__(self):
        self.indications = 0

    @abc.abstractmethod
    def get_indications(self):
        return self.indications

    @abc.abstractmethod
    def emulate(self):
        pass