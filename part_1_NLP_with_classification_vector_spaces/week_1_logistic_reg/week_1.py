#!/usr/bin/env python3

from spacy.tokens.token import Token
import validators
from pprint import pprint
from typing import Iterator, Iterable, Dict, Tuple
from operator import itemgetter
from collections import Counter
from nltk.stem.snowball import SnowballStemmer

import numpy as np
from tools.collections_wrappers import group_by
from tools import nlp

POSITIVE, NEGATIVE = 1, 0
Tweet = Tuple[str, int]
Word = str


def main():
    raw_tweets = [
        ("I am happy Because I am learning NLP", POSITIVE),
        ("I am happy", POSITIVE),
        ("@YMourri and @AndrewYNg are tuning a GREAT AI model at https://deeplearning.ai!!!", POSITIVE),
        ("I hated the movie", NEGATIVE),
        ("I am sad, I am not learning NLP", NEGATIVE),
        ("I am sad", NEGATIVE),
    ]
    tweets = [tweet for tweet, label in raw_tweets]
    labels = [label for tweet, label in raw_tweets]
    m = len(raw_tweets)

    freqs = build_freqs(tweets, labels)
    X = np.zeros([m, 3])
    for i in range(m):
        p_tweet = process_tweet(tweets[i])
        X[i, :] = extract_features(p_tweet, freqs)

    pprint(X)


def build_freqs(tweets: Iterable[str], labels: Iterable[int]) -> Dict[int, Dict[Word, int]]:
    class_to_word_to_freq = {}
    grouped_tweets = group_by(zip(tweets, labels), key=itemgetter(1))
    for id_class, group_tweets in grouped_tweets.items():
        counter = Counter(
            word
            for tweet, _ in group_tweets
            for word in process_tweet(tweet)
        )
        class_to_word_to_freq[id_class] = counter
    return class_to_word_to_freq


def process_tweet(s: str) -> Iterable[Word]:
    stemmer = SnowballStemmer(language="english")

    for token in nlp(s):
        if token.pos_ in ["PUNCT"]:
            continue
        if token.text.startswith("@"):
            continue
        if validators.email(token.text):
            continue
        if validators.url(token.text):
            continue
        yield stemmer.stem(token.lemma_)


def extract_features(p_tweet: Iterable[Word], freqs: Dict[int, Dict[Word, int]]):
    pos_freq = sum(
        freqs[POSITIVE].get(word, 0)
        for word in p_tweet
    )
    neg_freq = sum(
        freqs[NEGATIVE].get(word, 0)
        for word in p_tweet
    )
    return [1, pos_freq, neg_freq]


if __name__ == '__main__':
    raise NotImplementedError
    main()
