
# coding: utf-8

# In[ ]:

import nltk
import random
from nltk.corpus import movie_reviews

corpus_list = []

corpus_list = [(list(movie_reviews.words(fileid)), category)
              for category in movie_reviews.categories()
              for fileid in movie_reviews.fileids(category)]

random.shuffle(corpus_list)
print(corpus_list[4])

entire_words_list = []
for word in movie_reviews.words():
    entire_words_list.append(word.lower())
    
entire_words_list = nltk.FreqDist(entire_words_list)
print(entire_words_list.most_common(50))
print(entire_words_list["Hello"])


# In[ ]:




# In[ ]:



