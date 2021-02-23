from runners.helpful_fn import CheckPalindrum

def p036():
    print("Double-base palindromes")
    limit = 1000000
    result = 0
    for i in range(1, limit, 2):
        base2= int(bin(i)[2:])
        if(CheckPalindrum(i) and CheckPalindrum(base2)):
            print(f"numbers: {i} \t >> {base2}")
            result += i

    return(f"p036 Ans: {result}")
