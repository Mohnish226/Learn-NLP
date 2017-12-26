#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 22:03:36 2017

@author: Mohnish_Devadiga
"""

#Conditional Frequency Distribution

import nltk

names = [("Group A","Paul"),("Group A","Mike"),("Group A","Katy"),
         ("Group B","Amy"),("Group B","Dan"),("Group B","Amy")
         ]

print(nltk.FreqDist(names))

print(nltk.ConditionalFreqDist(names))