#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 20:57:13 2021

@author: whoami
"""

# we use the ord and chr functions
# print(ord('A'))

# print(chr(65))

def textToAscii(word):
    wordlist=list()
    for letter in word:
        wordlist.append(ord(letter))
    return wordlist

def asciiToText(ascii_text):
    reverse_word=list()
    name=''
    for num in ascii_text:
        num=chr(num)
        reverse_word.append(num)
    return name.join(reverse_word)
    
        
if __name__=='__main__':
    word=input('Ente a word: \n')
    print(textToAscii(word))
    print(asciiToText(textToAscii(word)))
                
    
        