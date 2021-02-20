#!/usr/bin/env python3

import os
import sys
import importlib

"""tree = os.listdir('.')
files = ['.git', 'README.md', 'main.py', 'runners', '.gitignore']
for f in files:
    if f in tree:
        tree.remove(f)"""
tree = ['p001', 'p002', 'p003', 'p004', 'p005']
for t in tree:
    mods = t + '.' + t
    x = importlib.import_module(mods)
    for attr in dir(x):
        if not attr.startswith('_'):
            globals()[attr] = getattr(x, attr)

def Euler():
    print("Welcome to project Euler\n")
    print("Choose Problem: \n")
    p = int(input("Enter problem number: "))
    if p < 9:
        problem = f"p00{p}"
        print(eval(problem)())


Euler()