#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 22:22:15 2018

@author: Mohnish_Devadiga
"""

import nltk
import urllib.request as ur
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Automatic_summarization"

html = ur.urlopen(url).read()

# Beautiful Soup

print("Org Data: \n")
print(html)

web_str = BeautifulSoup(html,"lxml").get_text()

start = web_str.find("Automatic data summarization is part of machine learning and data mining.")

end = web_str.find("For surveillance videos, one might want to extract the important events from the uneventful context.")

last_sent = len("For surveillance videos, one might want to extract the important events from the uneventful context.")

intro = web_str[start:end+last_sent]

intro_token = nltk.word_tokenize(intro)

print("\n\nData")
print(intro_token)