import datetime

from crowlizer_api.models.infra.date.systemdatetime import SystemDatetime
from crowlizer_api.models.infra.dtos.abstract_json_dto import AbstractJsonDto


class InferenceInputDto(AbstractJsonDto):

    def __init__(self):
        self.targetAmount: int = 0
        self.startDate: datetime.datetime = SystemDatetime.INIT_DATETIME.value
        self.endDate: datetime = SystemDatetime.INIT_DATETIME.value
        self.method: str = ''
        self.category: str = ''
        self.title: str = ''
        self.description: str = ''
        self.numImages: int = 0
        self.numVideos: int = 0
        self.twitterExistence: bool = False
        self.twitterFriends: int = 0
        self.twitterFollowers: int = 0
        self.facebookExistence: bool = False
        self.instagramExistence: bool = False
        self.webPageExistence: bool = False
