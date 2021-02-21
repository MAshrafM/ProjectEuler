"""
    Problem 21
    Amicable numbers
"""
from runners.helpful_fn import PrimeGen

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
def p021():
    print("Amicable numbers")  
    UpperLimit = 10000
    prms = PrimeGen(UpperLimit)
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
    return(f"p021 Ans: {sumAmicible}")
