# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZDWyzH5U8C61PCEpRQKL4IUPJyh2nUax
"""



import difflib
from difflib import SequenceMatcher

word = input('enter a word. ')
def suggestions(word):
   A = word
   A = A.lower()
   if A in data:
      for i in data:
        if i == A:
           B = data[A]
           return str(data[A])[1:-1]
   for i in data:
      if SequenceMatcher(None,i,word).ratio() > 0.8:
        A = input(f"did u mean {i}? press Y for yes,N for No ")
        if str(A) == 'Y':
          return str(data[i])[1:-1]
        else:
          return "try again"
   return "word not found"
      
suggestions(word)

