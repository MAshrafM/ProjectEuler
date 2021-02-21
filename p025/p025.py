"""
Using Computation by Rounding
https://en.wikipedia.org/wiki/Fibonacci_number#Computation_by_rounding'=
And the Golden Ration formula
https://en.wikipedia.org/wiki/Golden_ratio
"""

import math

def p025():
    print("1000-digit Fibonacci number")
    phi = ((1 + math.sqrt(5))/2)
    n = math.log(10, phi) * (math.log(math.sqrt(5), 10) + 999)


    print(f"P025 Ans: {math.ceil(n)}")