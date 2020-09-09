import pandas as pd
from typing import Tuple, List, Any


class FeatureEngineeringProcessor:

    @staticmethod
    def split_date(df: pd.DataFrame, cols_of_date: List[str]) -> Tuple[pd.DataFrame, List[str]]:
        new_feature_cols = []
        for col in cols_of_date:
            col_of_month = '{}Month'.format(col)
            col_of_day = '{}Day'.format(col)
            df[col_of_month] = pd.to_datetime(df[col]).dt.month
            df[col_of_day] = pd.to_datetime(df[col]).dt.day
            new_feature_cols.extend([col_of_month, col_of_day])
        new_df = df.copy()
        return new_df, new_feature_cols

    @staticmethod
    def compute_period(df: pd.DataFrame, col_of_start_date: str, col_of_end_date: str) -> Tuple[
        pd.DataFrame, List[str]]:
        new_feature_cols = ['period']
        df[new_feature_cols[0]] = (df[col_of_end_date] - df[col_of_start_date]).dt.days
        new_df = df.copy()
        return new_df, new_feature_cols

    @staticmethod
    def measure_len_of(df: pd.DataFrame, cols_to_measure_len: List[str]) -> Tuple[pd.DataFrame, List[str]]:
        new_feature_cols = []
        for col in cols_to_measure_len:
            col_of_len = '{}Len'.format(col)
            df[col_of_len] = df[col].str.len()
            new_feature_cols.append(col_of_len)
        new_df = df.copy()
        return new_df, new_feature_cols
