from typing import Dict

from crowlizer_api.models.domain.inference_input_dto import InferenceInputDto
from crowlizer_api.models.infra.design.singleton import Singleton


class InferenceRequestConverter(Singleton):

    @staticmethod
    def json2input(json_data: Dict[str, str]) -> InferenceInputDto:
        input_dto = InferenceInputDto()
        input_dto.import_json(json_data)
        return input_dto
