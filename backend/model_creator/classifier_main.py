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


def clustering_by_topic_model(df, col, num_topics=2):
    train_texts = tfidf_vectorizer(df, col)

    # モデル作成
    print('\nMODELING...')
    dictionary = Dictionary(train_texts)
    corpus = [dictionary.doc2bow(text) for text in train_texts]
    lda = LdaModel(corpus=corpus, num_topics=num_topics, id2word=dictionary)
    for i in range(num_topics):
        df['topic_{}'.format(i)] = 0

    # 推論
    print('\nPREDICTING...')
    score_by_topic = defaultdict(int)
    for i, doc in enumerate(corpus):
        # print(doc, end='\t')
        for topic, score in lda[doc]:
            df['topic_{}'.format(topic)].iloc[i] = float(score)
    return df


path = './20200605_closed_projects_df.csv'
df = pd.read_csv(path, encoding='shift_jis', engine='python', index_col=None)

target_col = 'success_prob'
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
df[target_col] = df['current_amount'] / df['target_amount']
df.loc[df[target_col] >= 1.0, target_col] = 1
df.loc[df[target_col] < 1.0, target_col] = 0

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
tfidf_df_seccess = vectorizer.fit_transform(df[df[target_col] == 1][text_col])
tfidf_df_fail = vectorizer.transform(df[df[target_col] == 0][text_col])
s = pd.concat([df[df[target_col] == 1].reset_index(drop=True), tfidf_df_seccess], axis=1)
f = pd.concat([df[df[target_col] == 0].reset_index(drop=True), tfidf_df_fail], axis=1)
df = pd.concat([s, f], axis=0)
# cols_to_train.extend(vectorizer.features_list)
df['tfidf-sum'] = np.sum(df[vectorizer.features_list], axis=1)
# one_hot_df = pd.DataFrame(data=np.where(tfidf_df > 0, 1, 0), columns=tfidf_df.columns)
# df = pd.concat([df, one_hot_df], axis=1)
# cols_to_train.extend(vectorizer.features_list)
# cols_to_target_encode.extend(vectorizer.features_list)

# 学習
print('train')
df[cols_to_target_encode] = df[cols_to_target_encode].astype(np.object)
X_train, X_test, y_train, y_test = train_test_split(df[cols_to_train], df[target_col], random_state=5, test_size=0.0001)
df_train = pd.concat([X_train, y_train], axis=1)
df_test = pd.concat([X_test, y_test], axis=1)

# target encoding
kf = KFold(5)
te = TargetEncoder(kf.split(df_train))
df_train.loc[:, cols_to_target_encode] = te.fit_transform(df_train[cols_to_target_encode], df_train[target_col])
df_test.loc[:, cols_to_target_encode] = te.transform(df_test[cols_to_target_encode])


params = {
    'n_estimators': 512,
    'max_depth': -1
}
result = run_experiment(params,
                        df_train[cols_to_train],
                        y_train,
                        df_test[cols_to_train],
                        type_of_target='binary',
                        with_auto_hpo=True)
for r in result.importance:
    print(r)
    print('\n')
print(result.test_prediction)
print(y_test)
print(sum(result.metrics) / len(result.metrics))
y_pred = np.where(result.test_prediction > 0.5, 1, 0)
print(accuracy_score(y_test, y_pred))
print(precision_score(y_test, y_pred))

for i, model in enumerate(result.models):
    with open('model_{}.pkl'.format(i), mode='wb') as fp:
        pickle.dump(model, fp)

with open('target_encoding.pkl', mode='wb') as fp:
    pickle.dump(te, fp)

with open('japanese_tfidf_vectorizer.pkl', mode='wb') as fp:
    pickle.dump(vectorizer, fp)
