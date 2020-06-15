from ..models.infra.abstract_request_dto import AbstractRequestDto


class InferenceRequestDto(AbstractRequestDto):

    def __init__(self):
        self.targetAmount = ''
        self.startDate = ''
        self.endDate = ''
        self.method = ''
        self.category = ''
        self.title = ''
        self.description = ''
        self.numImages = ''
        self.numVideos = ''
        self.twitterExistence = ''
        self.twitterFriends = ''
        self.twitterFollowers = ''
        self.facebookExistence = ''
        self.instagramExistence = ''
        self.webPageExistence = ''
