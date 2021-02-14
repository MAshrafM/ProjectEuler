from re import search
from math import sqrt

def primes_sieve(limit):
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []

    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in range(i*2, limitn, i):
            not_prime[f] = True

        primes.append(i)

    return primes

prms = primes_sieve(1500000)

def is_prime(n):
    n = int(n)
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(sqrt(n))
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

def is_trunc(n):
    for d in range(1, len(str(n))):
        if not is_prime(str(n)[d:]) or not is_prime(str(n)[:d]): 
            return False 
    return True

primes = []

idx = 4
while(len(primes) < 11):
    idx += 1
    #if not search('[245680]', str(prms[idx])):
    if(is_trunc(prms[idx])):
        primes.append(prms[idx])
        print(primes)


print("sum : ", sum(primes))
