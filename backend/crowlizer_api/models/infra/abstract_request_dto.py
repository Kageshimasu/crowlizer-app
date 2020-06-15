import logging
from abc import ABCMeta


class AbstractRequestDto(metaclass=ABCMeta):

    def import_json(self, json_data):
        logger = logging.getLogger(__name__)
        for key, _ in self.__dict__.items():
            if key in json_data:
                self.__dict__[key] = str(json_data[key])
            else:
                logger.debug('Key "%s" does not exist in the input json', key)
