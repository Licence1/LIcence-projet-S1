#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 16:22:33 2024

@author: parumeau
"""

for a in  [1,2,3,4,5]:
    for b in [1,2,3,4,5]:
        print(a,b)
        
        
        
        
def nbPairsListe(L):
    s = 0
    for elt in L:
        if elt == 0:
            s = s 
        else:
            if elt % 2 == 0 :
                s = s + 1
    return s
    