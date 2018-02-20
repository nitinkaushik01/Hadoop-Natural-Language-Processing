
# coding: utf-8

# In[6]:

import nltk
from nltk.corpus import inaugural
from nltk.tokenize import PunktSentenceTokenizer
nltk.data.path.append('F:/nltk_files/')

train_dataset = inaugural.raw('1789-Washington.txt')
test_dataset = inaugural.raw('1793-Washington.txt')

punkt_tokenizer = PunktSentenceTokenizer(train_dataset)
tokenized_text = punkt_tokenizer.tokenize(test_dataset)

def find_ner():
    try:
        for i in tokenized_text:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            namedEnt = nltk.ne_chunk(tagged, binary=False)
            namedEnt.draw()

    except Exception as e:
        print(str(e))
        
find_ner()


# In[ ]:




# In[ ]:



