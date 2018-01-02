#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 22:46:04 2018

@author: Mohnish_Devadiga
"""

import nltk

text = "I will go to the coffee shop in New York after I get off the jet plane"

text_tag = nltk.pos_tag(nltk.word_tokenize(text))

sequence = '''
            Chunk:
            {<NNPS>+}
            {<NNP>+}
            {<NN>+}
            '''
            
NPChunker = nltk.RegexpParser(sequence)

result = NPChunker.parse(text_tag)

print(result)