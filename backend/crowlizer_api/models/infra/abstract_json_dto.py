from abc import ABCMeta


class AbstractJsonDto(metaclass=ABCMeta):
    def to_json(self):
        return self.__dict__
