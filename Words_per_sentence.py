#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 11:00:43 2017

@author: Mohnish_Devadiga
"""

import nltk
from nltk.corpus import inaugural
import pandas as pd
import matplotlib 

inaugural.fileids()

#print(inaugural.fileids())

for speech in inaugural.fileids():
    word_count_total = len(inaugural.words(speech))
    print(speech , word_count_total)
    
#Go through all speech     
speech_length = [(len(inaugural.words(speech)), speech)for speech in inaugural.fileids()]

print(speech_length)

#Get the max and min speech
print("Max is : ",max(speech_length))
print("Min is : ",min(speech_length))

#Avg no of words per sentence for each speech
for speech in inaugural.fileids():
    word_total = len(inaugural.words(speech))
    Sents_total = len(inaugural.sents(speech))
    print((word_total/Sents_total),speech)
    

#Creating a Data Frame of the Speech
data = pd.DataFrame([int(speech[:4]), len(inaugural.words(speech))/len(inaugural.sents(speech))] for speech in inaugural.fileids())
print(data.head())

#Adding Column Names
data.columns = ["Year","Avg WPS"]

print(data)

#Use Matplotlib
data.plot("Year", figsize=(15,5))
