"""
    Problem 20
    Factorial digit sum
"""
import math

number = math.factorial(100) #100!
sums = 0  # Sum of digits
while(number > 0):
    digit = number%10
    sums += digit
    number //= 10

#Output
print("p20 Ans: ", sums)
