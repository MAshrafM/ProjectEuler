from re import search
from math import sqrt
from runners.helpful_fn import PrimeGen, CheckPrime

prms = PrimeGen(1500000)

def is_trunc(n):
    for d in range(1, len(str(n))):
        if not CheckPrime(str(n)[d:]) or not CheckPrime(str(n)[:d]): 
            return False 
    return True

def p037():
    print("Truncatable primes")
    primes = []
    idx = 4
    while(len(primes) < 11):
        idx += 1
        #if not search('[245680]', str(prms[idx])):
        if(is_trunc(prms[idx])):
            primes.append(prms[idx])
            print(f"Truncable prime: {primes}")


    return(f"p037 Ans: {sum(primes)}")
