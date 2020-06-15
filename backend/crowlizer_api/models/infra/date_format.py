import datetime

from .singleton import Singleton


class DateFormat(Singleton):

    @staticmethod
    def yyyyMMddTHH_mm_ss_Z(date_str: str):
        return datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%fZ')

    @staticmethod
    def yyyyMMdd(date_str: str):
        return datetime.datetime.strptime(date_str, '%Y-%m-%d')
