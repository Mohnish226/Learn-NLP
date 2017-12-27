#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 22:11:51 2017

@author: Mohnish_Devadiga
"""

import nltk
from nltk.util import ngrams

def print_ngram(ngram):
    print("\n== Printing ==\n")
    for item in ngram:
        print(item)
    return 0


text = "I think it might rain today."

tokens = nltk.word_tokenize(text)
print(tokens)

#Bigram
bigrams = nltk.bigrams(tokens)
print_ngram(bigrams)
    
print("\nTrigrams")
#Trigrams
trigrams = nltk.trigrams(tokens)

for item in trigrams:
    print(item)
    
text2 = "If it is nice out, I will go to the beach."

tokens2 = nltk.word_tokenize(text2)

bigrams2 = ngrams(tokens2,2)
print_ngram(bigrams2)

fourgrams = ngrams(tokens2,4) 
print_ngram(fourgrams)


