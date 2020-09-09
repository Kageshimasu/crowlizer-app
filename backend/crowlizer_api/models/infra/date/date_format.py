import datetime
import re
from enum import Enum


class _DateFormat:

    def __init__(self, regex: str, format: str):
        """
        :param regex:
        :param format:
        """
        self.regex = regex
        self.format = format


class DateFormat(Enum):
    yyyyMMdd = _DateFormat(r'^[0-9]{4}-([1-9]|0[1-9]|1[0-2])-([1-9]|0[1-9]|[12][0-9]|3[01])$', '%Y-%m-%d')

    def match(self, string: any) -> bool:
        return re.match(self.value.regex, str(string)) is not None

    def to_datetime(self, date_str: str) -> datetime.datetime:
        return datetime.datetime.strptime(date_str, self.value.format)
