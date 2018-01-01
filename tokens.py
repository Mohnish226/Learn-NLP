#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 21:11:34 2018

@author: Mohnish_Devadiga
"""

import nltk


#Word Token
my_string = "I am learning Natural Language Processing."

tokens = nltk.word_tokenize(my_string)

print(tokens)

print(len(tokens))

#Sentence Token
phrase = "I am learning Natural Language Processing. I am learning how to tokenize!"

token_sent = nltk.sent_tokenize(phrase)

print(token_sent)

print(len(token_sent))

for item in token_sent:
    print(nltk.word_tokenize(item))