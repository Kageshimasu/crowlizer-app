from ..domain.anaylsis_columns import AnalysisColumns
from ..infra.ml.feature_engineering_processor import FeatureEngineeringProcessor
from ..infra.ml.predict_processor import PredictProcessor
from ..infra.ml.nl_processor import NLProcessor
from ..domain.inference_repository import InferenceRepositoy


class InferenceProcessor:

    @staticmethod
    def extract_features(df):
        df, cols = FeatureEngineeringProcessor.split_date(df, AnalysisColumns.DATE_COLS.list())
        # InferenceProcessor._extend_list_to_train(cols)

        df, cols = FeatureEngineeringProcessor.compute_period(
            df, AnalysisColumns.START_DATE.str(), AnalysisColumns.END_DATE.str())
        InferenceProcessor._extend_list_to_train(cols)

        # df, cols = FeatureEngineeringProcessor.measure_len_of(df, AnalysisColumns.TEXT_COLS.list())
        # InferenceProcessor._extend_list_to_train(cols)

        df[AnalysisColumns.TITLE_DESCRIPTION.str()] = \
            df[AnalysisColumns.TITLE.str()] + df[AnalysisColumns.DESCRIPTION.str()]
        df, cols = NLProcessor.vectorize_with_load(
            InferenceRepositoy.get_nlprocessor_path(), df, AnalysisColumns.TITLE_DESCRIPTION.str())
        InferenceProcessor._extend_list_to_train(cols)

        featured_df = df.copy()
        return featured_df

    @staticmethod
    def predict(df, trained_model_paths, objective, cols_to_pred):
        pred_processor = PredictProcessor(trained_model_paths, objective)
        logit = pred_processor.predict(df[cols_to_pred])
        return logit

    @staticmethod
    def _extend_list_to_train(cols_to_extend):
        AnalysisColumns.SUCCESS_PROB_COLS.extend(cols_to_extend)
        AnalysisColumns.TARGET_AMOUNT_COLS.extend(cols_to_extend)
