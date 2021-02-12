import math
from re import search


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

prms = primes_sieve(1000000)


def rotate(s):
    return [s[n:] + s[:n] for n in range(1, len(s))]

#make a set of primes < L and remove any that have {0,2,4,5,6,8} except 2 and 5
primes = set(['2','5']+[str(p) for p in prms if not search('[024568]', str(p))])

n_circular_primes = sum(all(pr in primes for pr in rotate(p)) for p in primes)

print(len(prms))
print ("Project Euler 35 Solution =", n_circular_primes)