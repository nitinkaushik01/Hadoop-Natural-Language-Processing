
import nltk
import random
from nltk.corpus import movie_reviews

corpus_list = []

corpus_list = [(list(movie_reviews.words(fileid)), category)
              for category in movie_reviews.categories()
              for fileid in movie_reviews.fileids(category)]

random.shuffle(corpus_list)

entire_words_list = []
for word in movie_reviews.words():
    entire_words_list.append(word.lower())
    
entire_words_list = nltk.FreqDist(entire_words_list)
features_wd = list(entire_words_list.keys())[:4000]

def locate_word_features(corpus):
    words_text = set(corpus)
    feature_set = {}
    for word in features_wd:
        feature_set[word] = (word in words)
    return feature_set

print((locate_word_features(movie_reviews.words('pos/cv000_29590.txt'))))

features = [(locate_word_features(reveue), category) for (reveue, category) in corpus_list]




