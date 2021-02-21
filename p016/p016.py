"""
    Problem 16
    Power digit sum
"""
def p016():
    print("Power digit sum")
    num = int(pow(2,1000)) # Given Number
    sum_digits = 0 # sum digits holder
    # looping through the digits
    while num > 0:
        sum_digits = sum_digits + int(num % 10)  # taking the units of the number
        num = num // 10  # reducing the number
        
    #Output
    return(f"p016 Ans: {sum_digits}")
