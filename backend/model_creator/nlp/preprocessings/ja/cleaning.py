# -*- coding: utf-8 -*-
import re
import string
from ...unicode_script.unicode_script_map import get_script_type
from ...unicode_script.unicode_script import ScriptType
from bs4 import BeautifulSoup

SYMBOL_REGEX = re.compile('[!"#$%&\'\\\\()*+,-./:;<=>?@[\\]^_`{|}~「」〔〕“”〈〉『』【】＆＊・（）＄＃＠。、？！｀＋￥％]')


def clean_text(text):
    replaced_text = text.lower()
    replaced_text = SYMBOL_REGEX.sub('', replaced_text)
    replaced_text = re.sub(r'[【】]', ' ', replaced_text)  # 【】の除去
    replaced_text = re.sub(r'[（）()]', ' ', replaced_text)  # （）の除去
    replaced_text = re.sub(r'[［］\[\]]', ' ', replaced_text)  # ［］の除去
    replaced_text = re.sub(r'[@＠]\w+', '', replaced_text)  # メンションの除去
    replaced_text = re.sub(r'https?:\/\/.*?[\r\n ]', '', replaced_text)  # URLの除去
    replaced_text = re.sub(r'　', ' ', replaced_text)  # 全角空白の除去
    replaced_text = re.sub(r'[!-~]', "", replaced_text)  # 半角記号,数字,英字
    replaced_text = re.sub(r'[︰-＠]', "", replaced_text)  # 全角記号
    replaced_text = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", replaced_text)
    replaced_text = "".join([c for c in replaced_text if get_script_type(c) != ScriptType.U_Common])
    return replaced_text


def clean_html_tags(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    cleaned_text = soup.get_text()
    cleaned_text = ''.join(cleaned_text.splitlines())
    return cleaned_text


def clean_html_and_js_tags(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    [x.extract() for x in soup.findAll(['script', 'style'])]
    cleaned_text = soup.get_text()
    cleaned_text = ''.join(cleaned_text.splitlines())
    return cleaned_text


def clean_url(html_text):
    """
    \S+ matches all non-whitespace characters (the end of the url)
    :param html_text:
    :return:
    """
    clean_text = re.sub(r'http\S+', '', html_text)
    return clean_text


def clean_code(html_text):
    """Qiitaのコードを取り除きます
    :param html_text:
    :return:
    """
    soup = BeautifulSoup(html_text, 'html.parser')
    [x.extract() for x in soup.findAll(class_="code-frame")]
    cleaned_text = soup.get_text()
    cleaned_text = ''.join(cleaned_text.splitlines())
    return cleaned_text
