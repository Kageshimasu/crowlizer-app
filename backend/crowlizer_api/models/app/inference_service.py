from ..domain.inference_input_dto import InferenceInputDto
from ..domain.inference_output_dto import InferenceOutputDto
from ..domain.anaylsis_columns import AnalysisColumns
from ..infra.ml.category_encoding_processor import CategoryEncodingProcessor
from ..domain.inference_processor import InferenceProcessor
from ..infra.ml.pre_processor import PreProcessor
from ..domain.inference_repository import InferenceRepositoy


class InferenceService:

    @staticmethod
    def infer(input_dto: InferenceInputDto) -> InferenceOutputDto:
        df = input_dto.to_df()
        encoder_path = InferenceRepositoy.get_encoder_path()
        classifier_paths = InferenceRepositoy.get_classifier_paths()
        regressor_paths = InferenceRepositoy.get_regressor_paths()

        # 特徴量ちゅしゅつ
        df = CategoryEncodingProcessor.encode_with_load(encoder_path, df, AnalysisColumns.ENCODED_COLS.list())
        df = PreProcessor.take_logarithm_of(df, AnalysisColumns.LOG_TAKEN_COLS.list())
        df = InferenceProcessor.extract_features(df)

        # 成功確率の推論
        success_prob = InferenceProcessor.predict(
            df, classifier_paths, 'binary', AnalysisColumns.SUCCESS_PROB_COLS.list())

        # 目標金額の推論
        target_amount_est = InferenceProcessor.predict(
            df, regressor_paths, 'continuous', AnalysisColumns.TARGET_AMOUNT_COLS.list())

        # 結果返却
        output_dto = InferenceOutputDto()
        output_dto.predicted_success_prob = success_prob
        output_dto.predicted_target_amount = target_amount_est

        return output_dto
