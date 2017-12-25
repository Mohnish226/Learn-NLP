#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 21:27:21 2017

@author: Mohnish_Devadiga
"""

import nltk

alice = nltk.corpus.gutenberg.words("carroll-alice.txt")

#Frequency Distribution
alice_fd = nltk.FreqDist(alice)

print(alice_fd)

#Specific Word
print(alice_fd["Rabbit"])

#Check Common Words: 15 Words
print(alice_fd.most_common(15))

#Word used only once
print(alice_fd.hapaxes())