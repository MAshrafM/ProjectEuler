"""
    Problem 002
    Even Fibonacci numbers
"""
def p002():
    print("Even Fibonacci numbers")
    num_1 = 0     # 1st number
    num_2 = 2     # 2nd number
    current = 0   # current even number in the sequence
    total = 0     # total sum of even number
    while num_2 < 4000000:
        current = (4 * num_2) + num_1   # Even number in Fib = 1st number + 4*2nd number
        total = total + num_2           # Sum of even number
        num_1 = num_2                   # Swap
        num_2 = current                 # Swap

    return(f"p002 Ans: {total}")
