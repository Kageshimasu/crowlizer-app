from ..domain.inference_input_dto import InferenceInputDto
from ..domain.inference_output_dto import InferenceOutputDto


class InferenceService:

    @staticmethod
    def infer(input_dto: InferenceInputDto) -> InferenceOutputDto:
        # 2. 入力データをチェックする
        # 3. カテゴリ変数や自然言語の前処理
        # 4. 成功確率の推論
        # 5. 目標金額の推論
        # 6. 結果返却
        return InferenceOutputDto()
