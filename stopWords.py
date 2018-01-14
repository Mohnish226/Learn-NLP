#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 12:43:56 2018

@author: Mohnish_Devadiga
"""

import nltk

alice = nltk.corpus.gutenberg.words("carroll-alice.txt")

alice = [word.lower() for word in alice if word.isalpha()]

alice_fd = nltk.FreqDist(alice)

alice_100 = alice_fd.most_common(100)

common_words = [word[0] for word in alice_100]

rel_data = set(common_words) - set(nltk.corpus.stopwords.words("English"))