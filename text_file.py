#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 23:39:25 2018

@author: Mohnish_Devadiga
"""
import nltk

di = open('data/dec-independence.txt')

di_text = di.read()
#print(di_text)

di_token = nltk.word_tokenize(di_text)

di_fd = nltk.FreqDist(di_token)