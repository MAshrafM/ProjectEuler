"""
    Problem 21
    Amicable numbers
"""

#Using prime divisors
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

# Getting the divisors of all number
def FindAllDivisors(x, prms):
    divList = []
    factor = []
    remain = x
    exp = 1
    divList.append(1)
    for i in range(0, len(prms)):
        if(prms[i]*prms[i] > x):
            for i in range(0, len(factor)):
                for j in range(i+1, len(factor)):                  
                    new = factor[i] * factor[j]
                    if(x%new == 0 and new not in divList):
                        divList.append(new)
                        if(x/new not in divList):
                            divList.append(x/new)
            return divList
        
        exp = 1
        while(remain%prms[i] == 0):
            factor.append(pow(prms[i],exp))
            if(pow(prms[i], exp) <= remain and pow(prms[i], exp) != divList[-1] ):
                divList.append(pow(prms[i],exp))
                if(pow(prms[i],exp) != x/pow(prms[i],exp)):
                    divList.append(x/pow(prms[i],exp))
            
            exp += 1
            remain /= prms[i]          
            
        if(remain == 1):
            for i in range(0, len(factor)):
                for j in range(i+1, len(factor)):
                    new = factor[i] * factor[j]
                    if(x%new == 0 and new not in divList):
                        divList.append(new)
                        if(x/new not in divList):
                            divList.append(x/new)
            return divList

    return divList

# P021  
UpperLimit = 10000
prms = eratosthenes(UpperLimit)
sumAmicible = 0
Dn1 = 1
Dn2 = 1

for i in range(2, UpperLimit):
    Dn1 = sum(FindAllDivisors(i, prms))
    if (Dn1 > i and Dn1 <= UpperLimit):
        Dn2 = sum(FindAllDivisors(Dn1, prms))
        if (Dn2 == i):
            sumAmicible += i + Dn1

# Output
print("p021 Ans: ", sumAmicible)
