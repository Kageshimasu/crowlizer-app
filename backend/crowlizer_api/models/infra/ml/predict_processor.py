import pickle
import pandas as pd
import numpy as np
import os
from typing import List


class PredictProcessor:

    def __init__(self, trained_model_paths: List[str], objective):
        if objective != 'binary' and objective != 'continuous':
            raise ValueError('Objective must be multiclass or regression but got {}'.format(objective))
        self._trained_models = self._load(trained_model_paths)
        self._objective = objective

    @staticmethod
    def _load(paths: List[str]) -> List:
        models = []
        for path in paths:
            _, ext = os.path.splitext(path)
            if ext != '.pkl':
                raise ValueError('Expect the extension but got {}'.format(ext))
            models.append(pickle.load(open(path, 'rb')))
        return models

    def predict(self, df: pd.DataFrame) -> np.ndarray:
        logits = []
        for model in self._trained_models:
            if self._objective == 'binary':
                logit = model.predict_proba(df)[:, 1]
            elif self._objective == 'continuous':
                logit = np.exp(model.predict(df))
            else:
                raise ValueError('Objective must be multiclass or regression but got {}'.format(self._objective))
            logits.append(logit)
        mean_logit = np.mean(logits)
        return mean_logit
