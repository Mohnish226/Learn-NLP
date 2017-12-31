#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 21:10:38 2017

@author: Mohnish_Devadiga
"""

import nltk
import re

def print_word(re_word):
    print("\n Printing")
    for item in re_word:
        print(item)

alice = nltk.corpus.gutenberg.words("carroll-alice.txt")

#Words that start with "new"
alice_new = set([word for word in alice if re.search("^new", word)])
print_word(alice_new)
    
#Ends with "ful"
alice_ful = set([word for word in alice if re.search("ful$",word)])
print_word(alice_ful)
    
#Contains "nn"
alice_nn = set([word for word in alice if re.search("^.*nn.*$",word)])
print_word(alice_nn)
    
#Starts with a vowel
alice_aeiou = set([word for word in alice if re.search("^[aeiou].+$",word)])
print_word(alice_aeiou)