from runners.helpful_fn import PrimeGen, CheckSquare

def p046():
    print("Goldbach's other conjecture")
    flag = True
    primes = PrimeGen(10000)
    idx = 1
    while flag:
        idx += 2
        jdx = 0
        flag = False
        while(idx >= primes[jdx]):
            temp = (idx - primes[jdx])/2
            if(CheckSquare(temp)):
                flag = True
                break
            jdx += 1
            
    return (f"p046 Ans: {idx}")