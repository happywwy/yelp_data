# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 22:38:33 2015

@author: wangwenya
"""
from nltk.tokenize import word_tokenize

review_data = open('all_review', 'r')
tokenize_data = open('tokenize_review', 'w')

review = review_data.read().splitlines()
count = 1

for line in review:
    print count
    word_list = word_tokenize(line)
    tokenize_data.write(' '.join(word for word in word_list) + '\n')
    count += 1
    
review_data.close()
tokenize_data.close()