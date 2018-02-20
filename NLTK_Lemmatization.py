
# coding: utf-8

# In[ ]:

from nltk.stem import WordNetLemmatizer

lemma = WordNetLemmatizer()

print(lemma.lemmatize("lions"))
print(lemma.lemmatize("radii"))
print(lemma.lemmatize("better", pos="a")) #It became a different word altogether as best
print(lemma.lemmatize("loud", pos="a"))
print(lemma.lemmatize("eat"))
print(lemma.lemmatize("eat",'v'))


# In[ ]:




# In[ ]:



