import logging
from django.conf import settings
from abc import ABCMeta


class AbstractChecker(metaclass=ABCMeta):

    @staticmethod
    def raise_as(error: Exception):
        if settings.DEBUG:
            logger = logging.getLogger(__name__)
            logger.warning('ERROR: %s, but did not raise the error because of debug mode', error)
            return None
        raise error
