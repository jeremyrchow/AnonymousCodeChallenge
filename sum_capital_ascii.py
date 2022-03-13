#!/usr/bin/env python

def sum_capital_ascii(s):    
    import string
    ascii_sum = 0
    for char in list(s):
        if char in string.ascii_uppercase:
            ascii_sum += ord(char)
    return ascii_sum
sum_capital_ascii('142ljFA')
        
