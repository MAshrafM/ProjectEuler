import math

#http://planetmath.org/FormulaForSumOfDivisors

maxlimit = 28123

prms = []
def eratosthenes(limit):
    
    if (limit >= 2): 
        prms.append(2)
    if (limit >= 3):
        sqrtlmt = int((math.sqrt(limit) - 3)) >> 1
        lmt = (limit - 3) >> 1
        bfsz = (lmt >> 5) + 1
        buf = []
        for i in range(0, bfsz):
            buf.append(0)
        k = int(sqrtlmt + 1)
        for i in range(0, k):
            if ((buf[i >> 5] and (1 << (i & 31))) == 0):
                p = i + i + 3;
                for j in range((p * p - 3) >> 1, lmt+1, p):
                    buf[j >> 5] |= 1 << (j & 31);
            
        for i in range(0, lmt+1):
            if ((buf[i >> 5] & (1 << (i & 31))) == 0):
                prms.append(i + i + 3);

eratosthenes(maxlimit)

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

def SumofFactor(x):
    factors = PrimeFactorization(x, prms)
    sums = 1
    for i in range(0, len(factors)):
        temp = (pow(factors[i][0], factors[i][1] + 1) - 1)/(factors[i][0] - 1)
        sums = sums * temp
        
    return sums
                   
def SumofProper(x):
        sums = SumofFactor(x)
        return sums - x
		
Abundant = []
for i in range(2, maxlimit + 1):
    if(SumofProper(i) > i):
        Abundant.append(i)
		
sums = {}
for i in range(len(Abundant)):
    for j in range(len(Abundant)):
        temp = Abundant[i] + Abundant[j]
        if temp > maxlimit:
            break
        sums[temp] = 1
result = (maxlimit * (maxlimit + 1))//2 - sum(sums.keys())
print (result)