#!/usr/bin/env python

def print_name():
    name = input("Please enter your name: ")
    if not name:
        name = 'Guest'
    print(f"Hello, {name}!")
print_name()
