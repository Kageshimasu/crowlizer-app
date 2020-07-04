import numpy as np
import pandas as pd
from typing import List


class PreProcessor:

    @staticmethod
    def take_logarithm_of(df: pd.DataFrame, cols_to_preprocess: List[str]) -> pd.DataFrame:
        df[cols_to_preprocess] = np.log1p(df[cols_to_preprocess])
        return df.copy()
