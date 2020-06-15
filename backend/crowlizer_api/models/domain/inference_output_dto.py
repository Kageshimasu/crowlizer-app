from ..infra.abstract_json_dto import AbstractJsonDto


class InferenceOutputDto(AbstractJsonDto):

    def __init__(self):
        self.predicted_target_amount: int = 0
        self.predicted_success_prob: float = .0
