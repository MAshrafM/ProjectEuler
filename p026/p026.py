import math
from runners.helpful_fn import PrimeGen
#http://en.wikipedia.org/wiki/Fermat%27s_little_theorem

def p026():
    print("Reciprocal cycles")
    prms = PrimeGen(1000)
    longest = 0
    maxd = 0
    digit = 0

    for i in prms:
        cnt = 0
        remain = 10%i
        limit = 1000
        while(remain != 1 and limit > 0):
            remain *= 10
            remain %= i
            cnt += 1
            limit -= 1
            
        if(cnt > longest and limit > 1):
            longest = cnt
            maxd = i

    print(f"longest recuring cycle:  {longest}")
    return(f"p026 Ans: {maxd}")

