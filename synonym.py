from itertools import chain
from nltk.corpus import wordnet

def word_synonym(input):

   synonyms = wordnet.synsets(input)
   lemmas = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
   return lemmas
   #print(lemmas)

#word_synonym('change')