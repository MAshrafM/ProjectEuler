"""
Using Computation by Rounding
https://en.wikipedia.org/wiki/Fibonacci_number#Computation_by_rounding'=
And the Golden Ration formula
https://en.wikipedia.org/wiki/Golden_ratio
"""

import math

phi = ((1 + math.sqrt(5))/2)
n = math.log(10, phi) * (math.log(math.sqrt(5), 10) + 999)


print(math.ceil(n))