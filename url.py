#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 23:24:36 2018

@author: Mohnish_Devadiga
"""

import nltk
import urllib.request as ur

url = "http://www.gutenberg.org/cache/epub/84/pg84.txt"

Frankenstein_str = ur.urlopen(url).read()
#print(Frankenstein_str[:49])

Frankenstein_token = nltk.word_tokenize(Frankenstein_str.decode("utf-8"))