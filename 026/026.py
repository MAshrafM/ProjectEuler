import math

#http://en.wikipedia.org/wiki/Fermat%27s_little_theorem

prms = []
"""
Eratosthenes
A Function for prime number generation
"""
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

eratosthenes(1000)

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

print("number is ", maxd, "recuring cycle : ", longest)

