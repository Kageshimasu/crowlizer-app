import pickle
import pandas as pd
import numpy as np
from typing import List, Tuple, Any


class NLProcessor:
    COL_NAME = 'tfidf-sum'

    @staticmethod
    def load(path: str):
        return pickle.load(open(path, 'rb'))

    @staticmethod
    def vectorize(vectorizer: Any, df: pd.DataFrame, col_to_vectorize: str) -> Tuple[pd.DataFrame, List[str]]:
        vectorized_df = vectorizer.transform(df[col_to_vectorize])
        df[NLProcessor.COL_NAME] = np.sum(vectorized_df, axis=1)
        return df.copy(), [NLProcessor.COL_NAME]

    @staticmethod
    def vectorize_with_load(path: str, df: pd.DataFrame, col_to_vectorize: str) -> Tuple[pd.DataFrame, List[str]]:
        return NLProcessor.vectorize(NLProcessor.load(path), df, col_to_vectorize)
