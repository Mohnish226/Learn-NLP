#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 17:21:55 2018

@author: Mohnish_Devadiga
"""

import nltk

text = "I walked to the cafe to buy a coffee before work."

tokens = nltk.word_tokenize(text)

# Parts of Speech Tagger
pos = nltk.pos_tag(tokens)
print(pos)

md = nltk.corpus.gutenberg.words("melville-moby_dick.txt")

md_norm = [word.lower() for word in md if word.isalpha()]

# Get only noun
md_tagset = nltk.pos_tag(md_norm, tagset = "universal")

md_noun = [word[0] for word in md_tagset if word[1]== "NOUN"]

print(md_noun[:5])

# Top 10 nouns

nouns_fd = nltk.FreqDist(md_noun)
print(nouns_fd.most_common(10))