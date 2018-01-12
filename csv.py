#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 22:54:22 2018

@author: Mohnish_Devadiga
"""

import nltk
import csv

comments = []

with open("data/reviews.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        comments.append(row)
        
token = [nltk.word_tokenize(str(entry)) for entry in comments]