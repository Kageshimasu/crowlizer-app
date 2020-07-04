import pandas as pd
import MeCab
from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer

from .nlp.preprocessings.ja.cleaning import clean_text
from .nlp.preprocessings.ja.normalization import normalize
from .nlp.preprocessings.ja.stopwords import get_stop_words, remove_stopwords


class JapaneseTfidfVectorizer:

    def __init__(self, tokenize=None):
        if tokenize is None:
            tokenize = self._tokenize
        self._vectorizer = TfidfVectorizer(tokenizer=tokenize)
        self.features_list = []

    def fit(self, df: pd.DataFrame):
        return self._vectorizer.fit(df)

    def transform(self, df: pd.DataFrame):
        words_matrix = self._vectorizer.transform(df)
        tfidf_df = pd.DataFrame(data=words_matrix.toarray(), columns=self.features_list)
        return tfidf_df

    def fit_transform(self, df: pd.DataFrame):
        words_matrix = self._vectorizer.fit_transform(df)
        self.features_list = [str(i) + '_word' for i in range(len(self._vectorizer.get_feature_names()))]
        tfidf_df = pd.DataFrame(data=words_matrix.toarray(), columns=self.features_list)
        return tfidf_df

    def _tokenize(self, text: str) -> List[str]:
        mt = MeCab.Tagger('')
        mt.parse('')
        word_list = []
        text = clean_text(text)
        text = normalize(text)
        node = mt.parseToNode(text)
        while node:
            fields = node.feature.split(",")
            if fields[0] == '名詞':  # or fields[0] == '動詞' or fields[0] == '形容詞'
                word = node.surface
                word_list.append(word)
            node = node.next
        return self._remove_stop_words(word_list)

    def _remove_stop_words(self, words: List[str]) -> List[str]:
        stop_words = get_stop_words(words)
        removed_words = remove_stopwords(words, stop_words)
        return removed_words
