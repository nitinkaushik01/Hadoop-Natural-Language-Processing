# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 18:40:29 2018

@author: Nitin
"""
import nltk
from nltk.tokenize import word_tokenize
import random
from nltk.classify import ClassifierI

class Classifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers
        
    def classify(self, features):
        for cls in self._classifiers:
            fts = cls.classify(features)
        return fts

nltk.data.path.append('F:/nltk_files')

pos_tweets = open('C:/Users/Nitin/All_NLTK_Data/pos_tweets.txt', 'r', encoding="utf8").read()
neg_tweets = open('C:/Users/Nitin/All_NLTK_Data/neg_tweets.txt', 'r', encoding="utf8").read()

corpus_list = []
entire_word_list = []
only_adjective = ["J"]
for tweet in pos_tweets.split('\n'):
    corpus_list.append((tweet, "positive"))
    words = word_tokenize(tweet)
    part_of_speech = nltk.pos_tag(words)
    for part in part_of_speech:
        if part[1][0] in only_adjective:
            entire_word_list.append(part[0].lower())

for tweet in neg_tweets.split('\n'):
    corpus_list.append((tweet, "negative"))
    words = word_tokenize(tweet)
    part_of_speech = nltk.pos_tag(words)
    for part in part_of_speech:
        if part[1][0] in only_adjective:
            entire_word_list.append(part[0].lower())
            
entire_word_list = nltk.FreqDist(entire_word_list)
features_wd = list(entire_word_list.keys())[:22000]

def locate_word_features(corpus):
    word_text = word_tokenize(corpus)
    feature_set = {}
    for word in features_wd:
        feature_set[word] = (word in word_text)
    return feature_set

features = [(locate_word_features(review), category) for (review, category) in corpus_list]

random.shuffle(features)

train_data = features[:13000]
test_data = features[13000:]

nltk_classifier = nltk.NaiveBayesClassifier.train(train_data)

nltk_accuracy = (nltk.classify.accuracy(nltk_classifier, test_data))*100

voted_class = Classifier(
        nltk_classifier
        )

def find_sentiment(text):
    features_sent = locate_word_features(text)
    return voted_class.classify(features_sent)































