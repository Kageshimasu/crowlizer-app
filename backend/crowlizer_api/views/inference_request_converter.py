from typing import Dict

from .inference_request_dto import InferenceRequestDto
from ..models.infra.singleton import Singleton
from ..models.domain.inference_input_dto import InferenceInputDto


class InferenceRequestConverter(Singleton):

    @staticmethod
    def json2request(json_data: Dict[str, str]) -> InferenceRequestDto:
        request_dto = InferenceRequestDto()
        request_dto.import_json(json_data)
        return request_dto

    @staticmethod
    def request2input(json_data: InferenceRequestDto) -> InferenceInputDto:
        pass
