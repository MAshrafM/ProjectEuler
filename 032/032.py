def is_pandigital(n, s=9):
    n=str(n);
    # Check if it holds all the digits from 0 - 9 and thus a pandigital num
    # by striping the passed number from the sequence of 0 - 9
    
    return len(n) == s and not '1234567890'[:s].strip(n)

p = set()
for i in range(2, 80):
    start = 1234 if i < 10 else 123 
    for j in range(start, 10000//i):
        # check the mulipand the muliplier and the product
        if is_pandigital(str(i) + str(j) + str(i*j)):
            p.add(i*j)
print(p)
print ("sum =", sum(p))