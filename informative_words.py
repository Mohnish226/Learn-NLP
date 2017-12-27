#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 21:37:28 2017

@author: Mohnish_Devadiga
"""

import nltk

alice = nltk.corpus.gutenberg.words("carroll-alice.txt")

alice_fd = nltk.FreqDist(alice)

#Getting 100 most common words
alice_fd_100 = alice_fd.most_common(100)

#Since it is tuple, we'll only need the word and not the number
alice_100 = [
        word[0]       #First of the tuple
        for word in alice_fd_100
        ]


moby = nltk.corpus.gutenberg.words("melville-moby_dick.txt")

moby_fd = nltk.FreqDist(moby)

moby_fd_100 = moby_fd.most_common(100)

moby_100 = [
        word[0]       
        for word in moby_fd_100
        ]

#Subtract the sets 
word = set(alice_100) - set(moby_100)