#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 20:47:48 2018

@author: Mohnish_Devadiga
"""

import nltk

text = open("data/example.txt").read()

text_tag = nltk.pos_tag(nltk.word_tokenize(text))

text_ch = nltk.ne_chunk(text_tag)

#printing Entities
for chunk in text_ch:
    if hasattr(chunk, 'label'):
        print(chunk.label()," ".join(c[0] for c in chunk.leaves()))
