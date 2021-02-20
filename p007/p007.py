import random
from runners.helpful_fn import isPrimeMiller, primePass
"""
    Problem 7
    10001st prime
"""
def p007():
    print("10001st prime  ")
    pdx = 3     #number iteration 
    number = 0  #prime number holder
    idx = 1     #prime counter

    # check if a number is prime till u find the 10001 prime
    while idx < 10001:
        if isPrimeMiller(pdx):
            idx += 1
            number = pdx
        pdx += 1

    return(f"p007 Ans: {number}")
