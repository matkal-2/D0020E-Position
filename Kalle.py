# -*- coding: cp1252 -*-
import random

def kalle(jag, du):
    lst,h = [2]*10, 0
    
    while jag < du:
         print jag*du
         lst[h] = jag*du
         h += 1
    return "Kalle är: " + lst
