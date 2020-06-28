from enum import Enum
from typing import List


class AnalysisColumns(Enum):
    TARGET_AMOUNT = 'targetAmount'
    METHOD = 'method'
    CATEGORY = 'category'
    IMAGES = 'numImages'
    VIDEOS = 'numVideos'
    TWITTER_EXISTENCE = 'twitterExistence'
    TWITTER_FRIENDS = 'twitterFriends'
    TWITTER_FOLLOWERS = 'twitterFollowers'
    FACEBOOK_EXISTENCE = 'facebookExistence'
    INSTAGRAM_EXISTENCE = 'instagramExistence'
    WEB_PAGE_EXISTENCE = 'webPageExistence'
    PERIOD = 'period'
    TITLE = 'title'
    TITLE_LEN = 'titleLen'
    DESCRIPTION = 'description'
    DESCRIPTION_LEN = 'descriptionLen'
    START_DATE = 'startDate'
    START_DATE_DAY = 'startDateDay'
    END_DATE = 'endDate'

    SUCCESS_PROB_COLS = [
        TARGET_AMOUNT,
        METHOD,
        CATEGORY,
        IMAGES,
        TWITTER_EXISTENCE,
        TWITTER_FRIENDS,
        TWITTER_FOLLOWERS,
        FACEBOOK_EXISTENCE,
        INSTAGRAM_EXISTENCE,
        WEB_PAGE_EXISTENCE,
        PERIOD,
        START_DATE_DAY,
        TITLE_LEN,
        DESCRIPTION_LEN
    ]
    TARGET_AMOUNT_COLS = [
        TARGET_AMOUNT,
        METHOD,
        CATEGORY,
        IMAGES,
        TWITTER_EXISTENCE,
        TWITTER_FRIENDS,
        TWITTER_FOLLOWERS,
        FACEBOOK_EXISTENCE,
        INSTAGRAM_EXISTENCE,
        WEB_PAGE_EXISTENCE,
        PERIOD,
        START_DATE_DAY,
        TITLE_LEN,
        DESCRIPTION_LEN
    ]
    ENCODED_COLS = [
        CATEGORY,
        METHOD
    ]
    LOG_TAKEN_COLS = [
        TARGET_AMOUNT,
        TWITTER_FOLLOWERS,
        TWITTER_FRIENDS
    ]
    DATE_COLS = [
        START_DATE,
        END_DATE
    ]
    TEXT_COLS = [
        TITLE,
        DESCRIPTION
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
