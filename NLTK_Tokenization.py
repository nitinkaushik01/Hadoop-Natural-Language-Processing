
# coding: utf-8

# In[ ]:

from nltk.tokenize import sent_tokenize, word_tokenize

# Movie buff speaks about 300 spartan = Movie called 300
# Archealogist speaks about 300 spartan = A group of Greek soldiers

example_text = "What a fine weather today? Wasn't it raining yesterday. I'm going for a long drive on Highway 1. Are you coming along?"

print(sent_tokenize(example_text))

print(word_tokenize(example_text))


for i in word_tokenize(example_text):
    print(i)

