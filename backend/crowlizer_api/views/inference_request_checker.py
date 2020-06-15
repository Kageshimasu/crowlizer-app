from .inference_request_dto import InferenceRequestDto
from ..models.infra.singleton import Singleton
from ..models.infra.date_format import DateFormat
from ..models.infra.abstract_checker import AbstractChecker


class InferenceRequestChecker(Singleton, AbstractChecker):

    def check(self, request_dto: InferenceRequestDto):
        if not request_dto.targetAmount.isdecimal():
            self.raise_as(ValueError('Target amount must be decimal'))
        if int(request_dto.targetAmount) <= 0:
            self.raise_as(ValueError('Target amount must be over 1'))
        start_date = DateFormat.yyyyMMdd(request_dto.startDate)
        end_date = DateFormat.yyyyMMdd(request_dto.endDate)
        if start_date >= end_date:
            self.raise_as(ValueError('Start date must be earlier than End date'))
