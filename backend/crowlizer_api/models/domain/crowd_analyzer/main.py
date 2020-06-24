import pandas as pd
import numpy as np
import tqdm
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold

from sklearn.metrics import accuracy_score, precision_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from nyaggle.experiment import run_experiment
from nyaggle.feature.nlp import BertSentenceVectorizer
from nyaggle.feature.category_encoder import TargetEncoder

import MeCab
from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaModel
from collections import defaultdict
from nlp.preprocessings.ja.cleaning import clean_text
from nlp.preprocessings.ja.normalization import normalize
from nlp.preprocessings.ja.stopwords import get_stop_words, remove_stopwords
from sklearn.feature_extraction.text import TfidfVectorizer


def remove_stop_words(words):
    stop_words = get_stop_words(words)
    removed_words = remove_stopwords(words, stop_words)
    return removed_words


def tokenize(text):
    mt = MeCab.Tagger('')
    mt.parse('')
    word_list = []
    # cleaning and normalize
    text = clean_text(text)
    text = normalize(text)
    node = mt.parseToNode(text)
    while node:
        fields = node.feature.split(",")
        if fields[0] == '名詞':  # or fields[0] == '動詞' or fields[0] == '形容詞'
            word = node.surface
            word_list.append(word)
        node = node.next
    return remove_stop_words(word_list)


def wakati_df(df, col):
    vectorizer = TfidfVectorizer(tokenizer=tokenize)
    words_matrix = vectorizer.fit_transform(df[col])
    # temp_words_list = [str(i) + '_word' for i in range(len(vectorizer.get_feature_names()))]
    # words_df = pd.DataFrame(data=words_matrix.toarray(), columns=temp_words_list)
    col_name = col + 'tfidf_sumup'
    words_df = pd.DataFrame(data=np.max(words_matrix.toarray(), axis=1), columns=[col_name])
    return pd.concat([df, words_df], axis=1), [col_name]


def wakati_len(df, col):
    word_len_col = col + 'word_len_col'
    word_list = []
    for i in range(len(df)):
        words = tokenize(df[col].iloc[i])
        word_list.append(len(words))
    words_df = pd.DataFrame(data=word_list, columns=[word_len_col])
    return pd.concat([df, words_df], axis=1), [word_len_col]


def clustering_by_topic_model(df, col, num_topics=2):
    train_texts = wakati_df(df, col)

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
    'twitter_existence',
    'twitter_friends',
    'twitter_followers',
    'facebook_existence',
    'instagram_existence',
    'web_page_existence',
    # 'title',
    # 'description'

    # new feature
    'period',
    'start_date_day',
    'title_len',
    'description_len',
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
# for col in cols_to_encode:
#     le = LabelEncoder()
#     le.fit(df[col])
#     df[col] = le.transform(df[col])
for col in date_cols:
    df[col] = pd.to_datetime(df[col])
df['target_amount'] = np.log(df['target_amount'])
df['twitter_followers'] = np.log(df['twitter_followers'])
df['twitter_friends'] = np.log(df['twitter_friends'])
df['period'] = (df['end_date'] - df['start_date']).dt.days
df['start_date_month'] = df['start_date'].dt.month
df['start_date_day'] = df['start_date'].dt.day
df['title_len'] = df['title'].str.len()
df['description_len'] = df['description'].str.len()
# df, words_cols = wakati_df(df, 'title')
# cols_to_train.extend(words_cols)
# bv = BertSentenceVectorizer(text_columns=text_cols, lang='jp')
# japanese_text_vector = bv.fit_transform(df)
# print(japanese_text_vector)

# 可視化
# sns.boxplot(x=target_col, y='description_len', data=df)
# sns.distplot(df['target_amount'])
# plt.show()
# exit()

# 学習
df[cols_to_target_encode] = df[cols_to_target_encode].astype(np.object)
X_train, X_test, y_train, y_test = train_test_split(df[cols_to_train], df[target_col], random_state=4, test_size=0.1)
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
                        df_test[cols_to_train])
for r in result.importance:
    print(r)
    print('\n')
print(sum(result.metrics) / len(result.metrics))
y_pred = np.where(result.test_prediction > 0.5, 1, 0)
print(accuracy_score(y_test, y_pred))
print(precision_score(y_test, y_pred))
