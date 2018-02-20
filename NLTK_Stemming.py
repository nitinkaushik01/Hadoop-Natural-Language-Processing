
# coding: utf-8

# In[ ]:

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

Port_Stem = PorterStemmer()
list_of_words = ["stump", "stumped", "stumping", "curate", "curator", "curating", "curated"]

for wd in list_of_words:
    print(Port_Stem.stem(wd))

sample_text = "Let's eat the food. I was eating some Pasta but then I've eaten up all the Noodles"
words = word_tokenize(sample_text)

for wd in words:
    print(Port_Stem.stem(wd))

