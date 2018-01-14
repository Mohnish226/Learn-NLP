#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 12:39:08 2018

@author: Mohnish_Devadiga
"""

import nltk

# List of all words
words = nltk.corpus.words.words()
print(len(words))

# List of Stop Words
stop_words = nltk.corpus.stopwords.words("English")
print(len(stop_words))

# http://www.nltk.org/nltk_data/