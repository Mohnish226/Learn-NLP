#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 23:15:49 2018

@author: Mohnish_Devadiga
"""

import nltk

alice = nltk.corpus.gutenberg.words("carroll-alice.txt")

alice = alice[:1000]

print(len(alice))

alice_str = "".join(alice)

new_file = open("data/export.txt", "w")

new_file.write(alice_str)
new_file.close()