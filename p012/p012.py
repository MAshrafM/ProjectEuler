"""
    Problem 12
    Highly divisible triangular number
"""
from runners.helpful_fn import PrimeGen


# Prime Factorization using the prime and its exponent
def primeFactor(num, arr):
    temp = 1
    remain = num
    # loop on all the primes in the sieve
    for idx in range(len(arr)):
        # if square of a number is bigger than it then it has no exponent
        if(arr[idx]*arr[idx] > num):
            return temp * 2
        exp = 1 # init exponent
        # if no remainder increase exponent
        while(remain%arr[idx] == 0):
            exp = exp + 1
            remain = remain/arr[idx]
        # set the factor
        temp = temp * exp
        # if remainder is 1 return the factor
        if(remain == 1):
            return temp
    # return the factor after loop finishes
    return temp

# Main Program
def p012():
    print("Highly divisible triangular number")
    # init variables
    number = 1
    index = 2
    counter = 0
    Deven = 2
    Dodd = 2
    primeList = PrimeGen(1000)

    # to get to 500 divisor
    while(counter < 500):
        if(index%2 == 0):
            Deven = primeFactor(index + 1, primeList)
        else:
            Dodd = primeFactor((index+1)/2, primeList)
        counter = Deven * Dodd
        index = index + 1
    # the number
    number = index * (index - 1) / 2
    #Output
    return(f"p012 Ans: {number}")
        
    
