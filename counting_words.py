#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 21:48:11 2017

@author: Mohnish_Devadiga
"""

import nltk


# Project Gutenberg
nltk.corpus.gutenberg.fileids()

#Selecting a book
md=nltk.corpus.gutenberg.words("melville-moby_dick.txt")

#First 8 Words
print(md[:8])

#Count occurance of a word 
print(md.count("whale"))

#To find unique words
md_set = set(md)
print(len(md_set))

#Average number of times a word is repeated
print(len(md)/len(md_set))

#Everything is treated as a list, Now we'll use it as a sentence
md_sents = nltk.corpus.gutenberg.sents("melville-moby_dick.txt")

print(len(md_sents))

#Average number of words in a sentence
print(len(md)/len(md_sents))