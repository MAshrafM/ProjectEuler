"""
    Problem 10
    Summation of primes
"""

# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# find prime numbers
def eratosthenes(limit):
    primes = []  #primes holder
    sieve = [0]* limit  # sieve to check primes

    # loop over given limit
    for idx in range(2, limit):
        # if the numer in the sieve skip to the next
        if sieve[idx]:
            continue
        # put in the sieve the non prime of a number
        for jdx in range(2*idx, limit, idx):
            sieve[jdx] = 1
        # what is left is the prime
        primes.append(idx)

    return primes


primeList = eratosthenes(2000000)
print("p010 Ans: ", sum(primeList))
            
