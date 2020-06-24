from crowlizer_api.models.domain.inference_input_dto import InferenceInputDto
from crowlizer_api.models.infra.design.singleton import Singleton
from crowlizer_api.models.infra.checker.abstract_checker import AbstractChecker


class InferenceRequestChecker(Singleton, AbstractChecker):

    def check(self, input_dto: InferenceInputDto):
        pass
        # if not input_dto.targetAmount.isdecimal():
        #     self.raise_as(ValueError('Target amount must be decimal'))
        # if int(input_dto.targetAmount) <= 0:
        #     self.raise_as(ValueError('Target amount must be over 1'))
        # start_date = DateFormat.yyyyMMdd(input_dto.startDate)
        # end_date = DateFormat.yyyyMMdd(input_dto.endDate)
        # if start_date >= end_date:
        #     self.raise_as(ValueError('Start date must be earlier than End date'))
