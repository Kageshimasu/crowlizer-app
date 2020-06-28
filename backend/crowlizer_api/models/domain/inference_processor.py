from ..domain.anaylsis_columns import AnalysisColumns
from ..infra.ml.feature_engineering_processor import FeatureEngineeringProcessor
from ..infra.ml.predict_processor import PredictProcessor


class InferenceProcessor:

    @staticmethod
    def extract_features(df):
        df, cols = FeatureEngineeringProcessor.split_date(df, AnalysisColumns.DATE_COLS.list())
        df, cols = FeatureEngineeringProcessor.compute_period(df, AnalysisColumns.START_DATE.str(), AnalysisColumns.END_DATE.str())
        df, cols = FeatureEngineeringProcessor.measure_len_of(df, AnalysisColumns.TEXT_COLS.list())
        featured_df = df.copy()
        return featured_df

    @staticmethod
    def predict(df, trained_model_paths, objective, cols_to_pred):
        pred_processor = PredictProcessor(trained_model_paths, objective)
        logit = pred_processor.predict(df[cols_to_pred])
        return logit
