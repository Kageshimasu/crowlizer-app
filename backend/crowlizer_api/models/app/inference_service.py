import pandas as pd

from ..domain.inference_input_dto import InferenceInputDto
from ..domain.inference_output_dto import InferenceOutputDto
from ..domain.anaylsis_columns import AnalysisColumns
from ..infra.ml.category_encoding_processor import CategoryEncodingProcessor
from ..infra.ml.feature_engineering_processor import FeatureEngineeringProcessor
from ..infra.ml.pre_processor import PreProcessor


class InferenceService:

    @staticmethod
    def infer(input_dto: InferenceInputDto) -> InferenceOutputDto:
        # 1. DataFrame作成
        df = input_dto.to_df()

        # 2. カテゴリ変数エンコード
        df = CategoryEncodingProcessor.encode_with_load('./', df, AnalysisColumns.TO_ENCODE.list())

        # 3. 前処理
        df = PreProcessor.take_logarithm_of(df, AnalysisColumns.TO_TAKE_LOG.list())

        # 4. 特徴量エンジニアリング
        new_feature_cols = []
        df, cols = FeatureEngineeringProcessor.split_date(
            df, AnalysisColumns.OF_DATE.list())
        new_feature_cols.extend(cols)
        df, cols = FeatureEngineeringProcessor.compute_period(
            df, AnalysisColumns.START_DATE.str(), AnalysisColumns.END_DATE.str())
        new_feature_cols.extend(cols)
        df, cols = FeatureEngineeringProcessor.measure_len_of(
            df, AnalysisColumns.OF_TEXT.list())
        new_feature_cols.extend(cols)
        AnalysisColumns.TO_ANALYZE_SUCCESS_PROB.extend(new_feature_cols)
        AnalysisColumns.TO_ANALYZE_TARGET_AMOUNT.extend(new_feature_cols)

        # 5. 成功確率の推論
        # params_for_c = {}
        # classifier = LightGbm(params_for_c)
        # success_prob = classifier(AnalysisColumns.TO_ANALYZE_SUCCESS_PROB.list())

        # 6. 目標金額の推論
        # params_for_r = {}
        # regressor = LightGbm(params_for_r)
        # target_estimation = regressor(AnalysisColumns.TO_ANALYZE_TARGET_AMOUNT.list())

        # 7. 結果返却
        # output_dto = InferenceOutputDto()
        
        return InferenceOutputDto()
