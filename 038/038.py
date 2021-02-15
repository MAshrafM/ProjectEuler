"""
Well, that rules out two digit integers 92 through 98 multiplied by (2, 3, 4) because they can’t make a 9-digit concatenated product.
And, rule out three digit integers 921 through 987 multiplied by (2, 3, 4) for the same reason.
Four digit integers 9213 through 9876 multiplied by (2, 3, 4) will yield a 9-digit number for only 2.
"""
def is_pandigital(n, s=9):
    n=str(n)
    return len(n)==s and not '1234567890'[:s].strip(n)

pandigital = []
for i in range(9487, 9213, -1):
    num = str(i*1) + str(i*2)
    if is_pandigital(num):
        pandigital.append(num)
        print (num)

print("Ans to 038: ", max(pandigital))