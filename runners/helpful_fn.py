"""
Helpful Functions
"""

from math import sqrt
import random

def PrimeGen(limit):
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

def Perm(n, s):
    
    if len(s)==1: return s
    q, r = divmod(n, Factorial(len(s)-1))
    return s[q] + perm(r, s[:q] + s[q+1:])
	
def Factorial(n):
    
    if n < 1:
        return 1
    else:
       number = n * Factorial(n-1)
       return number

	   
def CheckPanda(n, s):
    n=str(n)
    return len(n)==s and not '1234567890'[:s].strip(n)
	
	
def CheckPrime(n):
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

def CheckPerm(a,b): 
	return sorted(str(a))==sorted(str(b))
	
def CheckPalindrum(n): 
	return str(n)==str(n)[::-1]

"""
 Primary Number test based on Miller Rabin Algorthim
 https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
"""
def isPrimeMiller(n):
    digits = n - 1
    pdx = 0

    while digits % 2 == 0:
        digits >>= 1 #shift binary > == divide by two
        pdx += 1 #increase index

    for jdx in range(20):
        temp = 0
        while temp == 0:
            temp = random.randrange(n)
        if not primePass(temp, pdx, digits, n):
            return False
    return True

def primePass(temp, pdx, digits, n):
    num_to_power = pow(temp, digits, n)
    if num_to_power == 1:
        return True
    for idx in range(pdx - 1):
        if num_to_power == n - 1:
            return True
        num_to_power = pow(num_to_power, 2, n)
    return num_to_power == n - 1