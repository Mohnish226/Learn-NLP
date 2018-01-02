#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 17:37:33 2018

@author: Mohnish_Devadiga
"""

import nltk

alice = nltk.corpus.gutenberg.words("carroll-alice.txt")

alice_norm = [word.lower() for word in alice if word.isalpha()]

alice_tag = nltk.pos_tag(alice_norm, tagset="universal")

alice_cfd = nltk.ConditionalFreqDist(alice_tag)

print(alice_cfd["over"]["ADV"])
print(alice_cfd["gloves"]["ADV"])
print(alice_cfd["savage"]["ADV"])