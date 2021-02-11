
def factorial(x):
    if(x == 0): return 1
    return x * factorial(x-1)

result = 0

for i in range(10, 100000):
    sums = 0
    num = i
    while(num > 0):
        d = num % 10
        num //= 10
        sums += factorial(d)

    if (sums == i):
        print(i)
        result += i

print (result)
