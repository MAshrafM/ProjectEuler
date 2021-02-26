from runners.helpful_fn import CheckPandigital, CheckPrime

def p041():
    print("Pandigital prime")
    n = 7654321
    while not(CheckPandigital(n, 7) and CheckPrime(n)):
        n -= 2
    return f"p041 Ans: {n}"
