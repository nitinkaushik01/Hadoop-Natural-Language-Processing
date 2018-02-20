
# coding: utf-8

# In[ ]:

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

sample_sent = "This is a very dumb question. Are you planning to go ahead and write a book of your own containing these questions."
stop_words_list = set(stopwords.words("english"))

word_list = word_tokenize(sample_sent)
non_stop_words = [word for word in word_list if not word in stop_words_list]

print(non_stop_words)


# In[ ]:



