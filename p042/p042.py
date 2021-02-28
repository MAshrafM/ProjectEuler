from math import sqrt

def isTriangle(n):
    temp = ((sqrt(1 + 8*n) - 1) / 2) % 1
    return not bool(temp)

def score(word):
    return sum(abs(64 - ord(l)) for l in word)

def p042():
    print("Code triangle numbers")
    name_ul = open("p042/p042_words.txt")
    name_ol = [x[1:-1] for x in name_ul.read().split(',')]
    name_ul.close()
    triangle = sum(isTriangle(score(word)) for word in name_ol)
    return(f"p042 Ans : {triangle}")
