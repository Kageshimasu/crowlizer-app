import pickle
import pandas as pd
from typing import List, Any


class CategoryEncodingProcessor:

    @staticmethod
    def load(path: str):
        return pickle.load(open(path, 'rb'))

    @staticmethod
    def encode(encoder: Any, df: pd.DataFrame, cols_to_encode: List[str]) -> pd.DataFrame:
        df[cols_to_encode] = encoder.transform(df[cols_to_encode])
        return df.copy()

    @staticmethod
    def encode_with_load(path: str, df: pd.DataFrame, cols_to_encode: List[str]) -> pd.DataFrame:
        return CategoryEncodingProcessor.encode(CategoryEncodingProcessor.load(path), df, cols_to_encode)
