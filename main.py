import os
import importlib
import runners

tree = os.listdir('.')
files = ['.git', 'README.md', 'main.py', 'runners']
for f in files:
    if f in tree:
        tree.remove(f)

for i in tree:
    mod = i+'.'+i
    importlib.import_module(mod)


def Euler():
    print("Welcome to project Euler\n")
    print("Choose Problem: \n")
    p = int(input("Enter problem number: "))
    if p < 9:
        problem = f"p00{p}"
        print(eval(problem)())


Euler()