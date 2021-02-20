"""
    Problem 10
    Summation of primes
"""
from runners.helpful_fn import PrimeGen

def p010():
    print("Summation of primes")
    primeList = PrimeGen(2000000)
    return(f"p010 Ans: {sum(primeList)}")
            
