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
    
#print(name_features("katy"))

name_list = [(names,'male')for name in names.words("male.txt")] + [(names,'female')for name in names.words("female.txt")]