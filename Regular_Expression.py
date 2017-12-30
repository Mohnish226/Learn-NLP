#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 21:10:38 2017

@author: Mohnish_Devadiga
"""

import nltk
import re

alice = nltk.corpus.gutenberg.words("carroll-alice.txt")

#Words that start with "new"
alice_new = set([word for word in alice if re.search("^new", word)])

for item in alice_new:
    print(item)
    
#Ends with "ful"
alice_ful = set([word for word in alice if re.search("ful$",word)])

for item in alice_ful:
    print(item)
    
#Contains "nn"
alice_nn = set([word for word in alice if re.search("^.*nn.*$",word)])

for item in alice_nn:
    print(item)
    
#Starts with a vowel
alice_aeiou = set([word for word in alice if re.search("^[aeiou].+$",word)])

for item in alice_aeiou:
    print(item)