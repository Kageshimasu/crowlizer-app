import logging
import pandas as pd
from typing import Dict, Any
from abc import ABCMeta

from crowlizer_api.models.infra.date.date_format import DateFormat


class AbstractJsonDto(metaclass=ABCMeta):

    def import_json(self, json_data: Dict[str, str]):
        logger = logging.getLogger(__name__)
        for key, _ in self.__dict__.items():
            if key in json_data:
                data = json_data[key]
                if DateFormat.yyyyMMdd.match(data):
                    self.__dict__[key] = DateFormat.yyyyMMdd.to_datetime(data)
                else:
                    self.__dict__[key] = type(self.__dict__[key])(data)
            else:
                logger.debug('Key "%s" does not exist in the input json', key)

    def to_json(self) -> Dict[str, Any]:
        return self.__dict__

    def to_df(self) -> pd.DataFrame:
        df = {}
        self_dict = self.to_json()
        for key in self_dict.keys():
            df[key] = [self_dict[key]]
        return pd.DataFrame(df)
