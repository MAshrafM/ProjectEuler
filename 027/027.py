import math

"""
Check if Number is a prime number
"""
def CheckPrime(num):
    if(num < 2 or (num > 2 and num%2 == 0)):
       return False
    elif (num == 2):
       return True
    else:
       temp = int(math.sqrt(num))
       for i in range(3, temp, 2):
           if(num%i == 0):
               return False
       return True

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
            print("Sequence of : ", primelength, "\t a : ", Coffa, "\t b : ", Coffb)

print("product ", Coffa * Coffb)