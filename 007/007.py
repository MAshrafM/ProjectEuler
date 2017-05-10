import random

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
#------------------------------------------------------------------------------

"""
    Problem 7
    10001st prime
"""

pdx = 3     #number iteration 
number = 0  #prime number holder
idx = 1     #prime counter

# check if a number is prime till u find the 10001 prime
while idx < 10001:
    if isPrimeMiller(pdx):
        idx += 1
        number = pdx
    pdx += 1

print("p007 Ans: ", number)
