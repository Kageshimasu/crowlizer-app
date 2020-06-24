import datetime
from enum import Enum


class SystemDatetime(Enum):
    INIT_DATETIME = datetime.datetime(1, 1, 1)

    def value_is(self, date: datetime.datetime) -> bool:
        return self.value == date
