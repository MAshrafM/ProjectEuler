"""
constructing a ring
                    7 8 9
                    6   2
                    5 4 3
for f(1) = 3 + 5 + 7 + 9
          (2n+1)^2 - 6n         
          (2n+1)^2 - 4n         
          (2n+1)^2 - 2n        
          (2n+1)^2      // Area of a Square       
          ---------------      
          >>4(2n+1)^2 – 12n     

A 1001*1001 = 500 rings


f(n) = 16/3x3 + 10x2 + 26/3x + 1
"""
import math
def p028():
    print("Number spiral diagonals")
    limit = 500
    sums = 1

    for i in range(1, 501):
        sums += 4* pow(2*i+1, 2) - 12*i

    return(f"p028 Ans: {sums}")
