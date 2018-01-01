#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 22:33:35 2018

@author: Mohnish_Devadiga
"""

import nltk

md = nltk.corpus.gutenberg.words("melville-moby_dick.txt")

# First 22 items
#print(md[:22])
md_22 = md[:22]
print(md_22)

# Getting only words

for item in md_22:
    if item.isalpha():
        print(item)
        
# Normalizing text
normal_text = [word.lower() for word in md_22 if word.isalpha()]

print(normal_text)

# Stemmers

# Porter
porter = nltk.PorterStemmer()

myList = ["cat","cats","lie","lying","run","running","city","cities","woman","women"]

print("\nPorter\n")
for word in myList:
    print(porter.stem(word))
    
# Lancaster   
lancaster = nltk.LancasterStemmer()
print("\nLancaster\n")
for word in myList:
    print(lancaster.stem(word))
    
# Word Net Lemmatizer
wnlem = nltk.WordNetLemmatizer()
print("\nWord Net Lemmatizer\n")
for word in myList:
    print(wnlem.lemmatize(word))
