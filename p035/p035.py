import math
from re import search
from runners.helpful_fn import PrimeGen, Rotate

def p035():
    print("Circular primes")
    prms = PrimeGen(10000)
    #make a set of primes < L and remove any that have {0,2,4,5,6,8} except 2 and 5
    primes = set(['2','5']+[str(p) for p in prms if not search('[024568]', str(p))])
    n_circular_primes = sum(all(pr in primes for pr in Rotate(p)) for p in primes)

    print(f"length of the prime array: {len(prms)}")
    return(f"P035 Ans: {n_circular_primes}")