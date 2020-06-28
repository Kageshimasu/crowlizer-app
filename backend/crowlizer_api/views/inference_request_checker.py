from ..models.domain.inference_input_dto import InferenceInputDto
from ..models.infra.design.singleton import Singleton
from ..models.infra.checker.abstract_checker import AbstractChecker
from ..models.domain.inference_repository import InferenceRepositoy


class InferenceRequestChecker(Singleton, AbstractChecker):

    def check(self, input_dto: InferenceInputDto):
        if int(input_dto.targetAmount) <= 0:
            self.raise_as(ValueError('targetAmount must be over 1'))
        if input_dto.method not in InferenceRepositoy.get_methods():
            self.raise_as(ValueError('method must be either all-in or all-or-nothing'))
        if input_dto.startDate >= input_dto.endDate:
            self.raise_as(ValueError('startDate must be earlier than End date'))
        if input_dto.numImages < 0:
            self.raise_as(ValueError('numImages must be over 0'))
        if input_dto.numVideos < 0:
            self.raise_as(ValueError('numVideos must be over 0'))
        if input_dto.twitterExistence not in [0, 1]:
            self.raise_as(ValueError('numVideos must be either 0 or 1'))
        if input_dto.twitterFriends < 0:
            self.raise_as(ValueError('twitterFriends must be over 0'))
        if input_dto.twitterFollowers < 0:
            self.raise_as(ValueError('twitterFollowers must be over 0'))
        if input_dto.facebookExistence not in [0, 1]:
            self.raise_as(ValueError('facebookExistence must be either 0 or 1'))
        if input_dto.webPageExistence not in [0, 1]:
            self.raise_as(ValueError('webPageExistence must be either 0 or 1'))
