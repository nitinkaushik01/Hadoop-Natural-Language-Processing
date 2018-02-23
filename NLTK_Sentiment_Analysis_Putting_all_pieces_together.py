import nltk
from nltk.tokenize import word_tokenize
import random
import pickle
from nltk.classify import ClassifierI


class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        for c in self._classifiers:
            v = c.classify(features)
        return v


nltk.data.path.append('F:/nltk_files')

pos_tweets = open('C:/Users/Nitin/All_NLTK_Data/pos_tweets.txt', 'r', encoding="utf8").read()
neg_tweets = open('C:/Users/Nitin/All_NLTK_Data/neg_tweets.txt', 'r', encoding="utf8").read()

corpus_list = []
for tweet in pos_tweets.split('\n'):
    corpus_list.append((tweet, "positive"))
    
for tweet in neg_tweets.split('\n'):
    corpus_list.append((tweet, "negative"))
    

entire_words_list = []
only_adjectives = ["J"]
for tweet in pos_tweets.split('\n'):
    corpus_list.append((tweet, "positive"))
    words = word_tokenize(tweet)
    part_of_speech = nltk.pos_tag(words)
    for part in part_of_speech:
        if part[1][0] in only_adjectives:
            entire_words_list.append(part[0].lower())
            
    

for tweet in neg_tweets.split('\n'):
    corpus_list.append((tweet, "negative"))
    words = word_tokenize(tweet)
    part_of_speech = nltk.pos_tag(words)
    for part in part_of_speech:
        if part[1][0] in only_adjectives:
            entire_words_list.append(part[0].lower())

#=======================Pickle Corpus_List and Entire_Word_List=========================            
#pickled_corpus_list = open("F:/Pickle/corpus_list.pickle","wb")
#pickle.dump(corpus_list, pickled_corpus_list)
#pickled_corpus_list.close()

#pickled_entire_words_list = open("F:/Pickle/pickled_entire_words_list.pickle","wb")
#pickle.dump(entire_words_list, pickled_entire_words_list)
#pickled_entire_words_list.close()
#=======================Pickle Corpus_List and Entire_Word_List========================
#=======================Unpickle Corpus_List and Entire_Word_List======================
#corpus_list_fl = open("F:/Pickle/corpus_list.pickle","rb")
#corpus_list = pickle.load(corpus_list_fl)
#corpus_list_fl.close()

#entire_words_list_fl = open("F:/Pickle/pickled_entire_words_list.pickle","rb")
#entire_words_list = pickle.load(entire_words_list_fl)
#entire_words_list_fl.close()
#=======================Unpickle Corpus_List and Entire_Word_List=====================
#=======================Pickle Features_wd============================================
#entire_words_list = nltk.FreqDist(entire_words_list)
#features_wd = list(entire_words_list.keys())[:22000]

#pickled_features = open("F:/Pickle/features.pickle","wb")
#pickle.dump(features_wd, pickled_features)
#pickled_features.close()
#=======================Pickle Features_wd============================================
#=======================Unpickle Features_wd==========================================
#features_fl = open("F:/Pickle/features.pickle","rb")
#features_wd = pickle.load(features_fl)
#features_fl.close()
#=======================Unpickle Features_wd==========================================

def locate_word_features(corpus):
    #words_text = set(corpus) # We are commenting out this because earlier we had words but now we are getting words in the form of a long string
    words_text = word_tokenize(corpus)
    feature_set = {}
    for word in features_wd:
        feature_set[word] = (word in words_text)
    return feature_set

features = [(locate_word_features(review), category) for (review, category) in corpus_list]

#random.shuffle(features)

#=======================Pickle Features============================================
#feat_fl = open("F:/Pickle/feat.pickle","wb")
#pickle.dump(features, feat_fl)
#feat_fl.close()
#=======================Pickle Features============================================
#=======================Unpickle Features==========================================
#feat = open("F:/Pickle/feat.pickle","rb")
#features = pickle.load(feat)
#feat.close()
#=======================Unpickle Features============================================
random.shuffle(features)

train_data = features[:13000]
test_data = features[13000:]

nltk_classifier = nltk.NaiveBayesClassifier.train(train_data)

#=======================Pickle NLTK_Classifier========================================
#nltk_classifier_fl = open("F:/Pickle/naivebayes.pickle","rb")
#nltk_classifier = pickle.load(nltk_classifier_fl)
#nltk_classifier_fl.close()
#=======================Pickle NLTK_Classifier========================================

nltk_accuracy = (nltk.classify.accuracy(nltk_classifier, test_data))*100
print("Model Accuracy:", nltk_accuracy)

#=======================Unpickle NLTK_Classifier========================================
#naive_bayes_classifier = open("F:/Pickle/naivebayes.pickle","wb")
#pickle.dump(nltk_classifier, naive_bayes_classifier)
#naive_bayes_classifier.close()
#=======================Unpickle NLTK_Classifier========================================

voted_classifier = VoteClassifier(
                                  nltk_classifier
                                  )

def find_sentiment(text):
    features_sent = locate_word_features(text)
    return voted_classifier.classify(features_sent)


