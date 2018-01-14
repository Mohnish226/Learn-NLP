#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 13:27:01 2018

@author: Mohnish_Devadiga
"""

import nltk
import csv
import numpy as np

negative = []

with open("data/words-negative.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        negative.append(row)
        
positive = []

with open("data/words-positive.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        positive.append(row)
        
def sentiment(text):
    temp = []
    text_sent = nltk.sent_tokenize(text)
    for sentence in text_sent:
        n_count = 0
        p_count = 0
        sent_word = nltk.word_tokenize(sentence)
        for word in sent_word:
            for item in positive:
                if word == item[0]:
                    #print(item)
                    p_count += 1
            
            for item in negative:
                if word == item[0]:
                    #print(item)
                    n_count += 1
                    
        if p_count > 0 and n_count == 0:
            #print("+: "+sentence)
            temp.append(1)
        elif n_count%2 > 0:
            #print("-: "+sentence)
            temp.append(-1)
        elif n_count%2 == 0 and n_count > 0:
            #print("+: "+sentence)
            temp.append(1)
        else:
            #print("?: "+sentence)
            temp.append(0)
   
    return temp

'''
# Test Sentiment()
print(sentiment("It was terribly bad."))
print(sentiment("This is a sentance about nothing."))
print(sentiment("Actualluty, it was not bad at all."))
'''

comments = []

with open("data/reviews.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        comments.append(row)
        
for review in comments:
    print("\n")
    print(np.average(sentiment(str(review))))
    print(review)