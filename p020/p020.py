"""
    Problem 20
    Factorial digit sum
"""
import math
def p020():
    print("Factorial digit sum")
    number = math.factorial(100) #100!
    sums = 0  # Sum of digits
    while(number > 0):
        digit = number%10
        sums += digit
        number //= 10

    #Output
    return(f"p20 Ans: {sums}")
