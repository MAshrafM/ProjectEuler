import math
from runners.helpful_fn import CheckPrime

def p027():
    print("Quadratic primes")
    Coffa = 0 #coefficient a placeholder
    Coffb = 0 #coefficient b placeholder
    primelength = 0 #length of prime


    for i in range(-999, 1000, 2):
        for j in range(1, 1000, 2):
            temp = 0
            while(CheckPrime(abs((temp * temp) + (i * temp) + j))):
                temp += 1
                
            if(temp > primelength):
                Coffa = i
                Coffb = j
                primelength = temp
                print(f"Sequence of :{ primelength}, \t a : {Coffa}, \t b : {Coffb}")

    return(f"p027 Ans: {Coffa * Coffb}")