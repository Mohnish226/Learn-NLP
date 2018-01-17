#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 21:26:30 2018

@author: Mohnish_Devadiga
"""

import nltk
import matplotlib
import matplotlib.pyplot as plt
import random
from nltk.corpus import names
from PIL import Image   

#print(names.fileids())
matplotlib.style.use("ggplot")

names_cfd = nltk.ConditionalFreqDist((fileid,name[-2:])for fileid in names.fileids() for name in names.words(fileid))

'''
plt.figure(figsize=(50,10))
image = names_cfd.plot()
'''

def name_features(name):
    return{"pair" : name[-2:]}
    
print(name_features("katy"))

name_list = ([(name, 'male') for name in names.words('male.txt')] + [(name, "female") for name in names.words('female.txt')])

print(name_list[:10])
print(name_list[-10:])

#Shuffle Data
random.shuffle(name_list)
print(name_list[:10])

features = [(name_features(name), gender) for (name,gender) in name_list]
print(features[:10])

print(len(features)/2)
training_set = features[:3972]
testing_set = features[3972:]

classifier = nltk.NaiveBayesClassifier.train(training_set)


male_names = names.words('male.txt')
"Carmello" in male_names

classifier.classify(name_features("Carmello"))

print(nltk.classify.accuracy(classifier, testing_set))