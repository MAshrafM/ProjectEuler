"""
    Problem 004
    Largest palindrome product
"""

# check if a number is a Palindrome
def isPalin(num):
    strings = str(num)
    reverseString = ""

    # reverse the number in a new variable
    for idx in range(len(strings) - 1, -1, -1):
        reverseString += strings[idx]

    # check palindrome
    return strings == reverseString

maxPal = 0

for idx in range(999, 99, -1):
    for jdx in range(idx-1, 99, -1):
        # multiply loop
        mul = idx * jdx
        if(isPalin(mul)):
            temp = mul
            # save only the max multiply
            if(temp > maxPal):
                maxPal = temp

# Output
print("p004 Ans : ", maxPal)


