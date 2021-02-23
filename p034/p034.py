
def factorial(x):
    if(x == 0): return 1
    return x * factorial(x-1)

def p034():
    print("Digit factorials")
    result = 0
    for i in range(10, 100000):
        sums = 0
        num = i
        while(num > 0):
            d = num % 10
            num //= 10
            sums += factorial(d)

        if (sums == i):
            print(f"number found:  {i}")
            result += i

    return(f"p034 Ans: {result}")
