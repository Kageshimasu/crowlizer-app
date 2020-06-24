from enum import Enum
from typing import List

class AnalysisColumns(Enum):
    TO_ANALYZE_SUCCESS_PROB = [
        'target_amount',
        'method',
        'category',
        'images',
        'twitter_existence',
        'twitter_friends',
        'twitter_followers',
        'facebook_existence',
        'instagram_existence',
        'web_page_existence',
        'period',
        'start_date_day',
        'title_len',
        'description_len'
    ]
    TO_ANALYZE_TARGET_AMOUNT = [
        'method',
        'category',
        'images',
        'twitter_existence',
        'twitter_friends',
        'twitter_followers',
        'facebook_existence',
        'instagram_existence',
        'web_page_existence',
        'period',
        'start_date_day',
        'title_len',
        'description_len'
    ]
    TO_ENCODE = [
        'category',
        'method',
    ]
    TO_TAKE_LOG = [
        'target_amount',
        'twitter_followers',
        'twitter_friends'
    ]
    START_DATE = 'start_date'
    END_DATE = 'end_date'
    OF_DATE = [
        START_DATE,
        END_DATE
    ]
    OF_TEXT = [
        'title',
        'description'
    ]

    def str(self) -> str:
        self._check_type_error('str', str)
        return self.value

    def list(self) -> List[str]:
        self._check_type_error('list', list)
        return self.value

    def append(self, new_str: str) -> List:
        self._check_type_error('append', list)
        return self.value.append(new_str)

    def extend(self, new_list: list):
        self._check_type_error('extend', list)
        self.value.extend(new_list)
        return self.value

    def _check_type_error(self, func_name, exp_type):
        this_type = type(self.value)
        if this_type is not exp_type:
            raise ValueError('{} function is only for {}, but got {}'.format(func_name, exp_type, this_type))
