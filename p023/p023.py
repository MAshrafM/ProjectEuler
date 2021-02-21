import math
from runners.helpful_fn import PrimeGen
#http://planetmath.org/FormulaForSumOfDivisors



def PrimeFactorization(x, list):
    
    factors = []
    exp = 1
    remain = x
    for i in range(0, len(list)):
            
            if(list[i] * list[i] > x and list[i] > remain):
                return factors
            
            exp = 1
            while(remain%list[i] == 0):
                remain /= list[i]
                exp = exp + 1
            if(exp > 1):
                #factors.append(pow(list[i], exp))
                factors.append([list[i], exp - 1])
            if(remain == 1):
                return factors
    
    return factors

def SumofFactor(x, primes):
    factors = PrimeFactorization(x, primes)
    sums = 1
    for i in range(0, len(factors)):
        temp = (pow(factors[i][0], factors[i][1] + 1) - 1)/(factors[i][0] - 1)
        sums = sums * temp
        
    return sums
                   
def SumofProper(x, primes):
        sums = SumofFactor(x, primes)
        return sums - x
		
def p023():
    print("Non-abundant sums")
    maxlimit = 28123
    primes = PrimeGen(maxlimit)
    Abundant = []
    for i in range(2, maxlimit + 1):
        if(SumofProper(i, primes) > i):
            Abundant.append(i)
            
    sums = {}
    for i in range(len(Abundant)):
        for j in range(len(Abundant)):
            temp = Abundant[i] + Abundant[j]
            if temp > maxlimit:
                break
            sums[temp] = 1
    result = (maxlimit * (maxlimit + 1))//2 - sum(sums.keys())
    return(f"Ans p023 : {result}")