from runners.helpful_fn import PrimeGen, PrimeFactorization

def p047():
    print("Distinct primes factors")
    primes = PrimeGen(100000)
    num_factor = 4
    num_consec = 4
    consec = 1
    num = 657
    while(consec != num_consec):
        num += 1
        factors = PrimeFactorization(num, primes)
        if(len(factors) == num_factor):
            consec += 1
        else:
            consec = 0
    return(f"p047 Ans: {num - 3}")
