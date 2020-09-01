import pandas as pd
import numpy as np
import pickle
import MeCab
from sklearn.model_selection import KFold

from sklearn.metrics import accuracy_score, precision_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from nyaggle.experiment import run_experiment
from nyaggle.feature.nlp import BertSentenceVectorizer
from nyaggle.feature.category_encoder import TargetEncoder

from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaModel
from collections import defaultdict
from model_creator.nlp.preprocessings.ja.cleaning import clean_text
from model_creator.nlp.preprocessings.ja.normalization import normalize
from model_creator.nlp.preprocessings.ja.stopwords import get_stop_words, remove_stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from model_creator.tfidf_vectorizer import JapaneseTfidfVectorizer


path = './20200605_closed_projects_df.csv'
df = pd.read_csv(path, encoding='shift_jis', engine='python', index_col=None)

target_col = 'current_amount'
success_prob = 'success_prob'
cols_to_train = [
    'target_amount',
    'method',
    'category',
    'images',
    # 'videos',
    # 'twitter_existence',
    'twitter_friends',
    'twitter_followers',
    # 'facebook_existence',
    # 'instagram_existence',
    # 'web_page_existence',

    # new feature
    'period',
    # 'start_date_day',
    # 'title_len',
    # 'description_len',
    'tfidf-sum',
    # 'tfidf_non_zero'
]
# dateとdescriptionが足りない
cols_to_need_to_fill = [
    'twitter_friends',
    'twitter_followers',
]
cols_to_target_encode = [
    'category',
    'method',
]
date_cols = [
    'start_date',
    'end_date'
]
text_cols = [
    'title'
]


# TARGET 編集
df[success_prob] = df['current_amount'] / df['target_amount']
df.loc[df[success_prob] >= 1.0, success_prob] = 1
df.loc[df[success_prob] < 1.0, success_prob] = 0

# 特徴量編集
for col in cols_to_need_to_fill:
    df[col] = df[col].fillna(-1)
for col in date_cols:
    df[col] = pd.to_datetime(df[col])
df['target_amount'] = np.log1p(df['target_amount'])
df['twitter_followers'] = np.log1p(df['twitter_followers'])
df['twitter_friends'] = np.log1p(df['twitter_friends'])
df['period'] = (df['end_date'] - df['start_date']).dt.days
df['start_date_month'] = df['start_date'].dt.month
df['start_date_day'] = df['start_date'].dt.day
zero_prob_df = df.sample(frac=0.2).reset_index()
zero_prob_df['title'] = ''
zero_prob_df['description'] = ''
zero_prob_df[target_col] = 0
df = pd.concat([df, zero_prob_df]).reset_index(drop=True)
df['title_len'] = df['title'].str.len()
df['description_len'] = df['description'].str.len()
text_col = 'title_description'
df[text_col] = df['title'] + df['description']
vectorizer = JapaneseTfidfVectorizer()
tfidf_df = vectorizer.fit_transform(df[text_col])
df['tfidf-sum'] = np.sum(tfidf_df, axis=1)
# df['tfidf_non_zero'] = np.log1p(np.count_nonzero(tfidf_df, axis=1))
# df = pd.concat([df, tfidf_df], axis=1)
# cols_to_train.extend(vectorizer.features_list)


# 学習
df[target_col] = np.log1p(df[target_col])
df[cols_to_target_encode] = df[cols_to_target_encode].astype(np.object)
cols_to_split = cols_to_train.copy()
cols_to_split.append(success_prob)
X_train, X_test, y_train, y_test = train_test_split(df[cols_to_split], df[target_col], random_state=4, test_size=0.01)
df_train = pd.concat([X_train, y_train], axis=1)
df_test = pd.concat([X_test, y_test], axis=1)

# target encoding
kf = KFold(5)
te = TargetEncoder(kf.split(df_train))
df_train.loc[:, cols_to_target_encode] = te.fit_transform(df_train[cols_to_target_encode], df_train[success_prob])
df_test.loc[:, cols_to_target_encode] = te.transform(df_test[cols_to_target_encode])

params = {
    'metric': 'rmse',
    'objective': 'regression',
    'n_estimators': 512,
    'max_depth': -1
}
result = run_experiment(params,
                        df_train[cols_to_train],
                        y_train,
                        df_test[cols_to_train],
                        type_of_target='continuous',
                        with_auto_hpo=True)
for r in result.importance:
    print(r)
    print('\n')
print(sum(result.metrics) / len(result.metrics))
print(result.submission_df)
print(y_test)

for i, model in enumerate(result.models):
    with open('model_{}.pkl'.format(i), mode='wb') as fp:
        pickle.dump(model, fp)
