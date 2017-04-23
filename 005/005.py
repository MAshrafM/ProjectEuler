"""
    Problem 005
    Smallest multiple

    Instead of Abrute force Implimentation
    The number is the product of the primes raised to the approriate power
"""

n = 20
primes = [2,3,5,7,11,13,17,19]
prime_powers = [0,0,0,0,0,0,0,0]

for idx in range(n+1):
    for jdx in range(len(primes)):
        a = idx
        m = 0
        p = primes[jdx]

        # if number divisiable by a prime count it to raise it to the power
        while a%p==0 and a!=0:
            a = a/p
            m += 1
        if m > prime_powers[jdx]:
            prime_powers[jdx] = m

product = 1
# multiply the primes raised to the approriate power
for kdx in range(len(primes)):
    product *= pow(primes[kdx],prime_powers[kdx])

# Output
print ("p005 Ans : ", product)
