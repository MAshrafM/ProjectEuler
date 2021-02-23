#!/usr/bin/env python3

import os
import sys
import importlib

def Euler():
    p = int(input("Enter problem number: "))
    if p < 10:
        problem = f"p00{p}"
        print(eval(problem)())
    elif p < 100:
        problem = f"p0{p}"
        print(eval(problem)())

def Welcome():
    print("#============================#")
    print("|  Welcome to project Euler  |")
    print("#============================#")
    print("Choose Problem:")
    print("___________________\n")

def Problems():
    tree = os.listdir('.')
    files = ['.git', 'README.md', '__main__.py', '__init__.py', '__pycache__','runners', '.gitignore']
    for f in files:
        if f in tree:
            tree.remove(f)


    for t in tree:
        mods = t + '.' + t
        x = importlib.import_module(mods)
        for attr in dir(x):
            if not attr.startswith('_'):
                globals()[attr] = getattr(x, attr)

Welcome()
Problems()
Euler()