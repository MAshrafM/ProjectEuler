"""
    p003
    Largest prime factor
"""
def p003():
    print("Largest prime factor")
    lowPF = 2 # start division with 2
    num = 600851475143 # provided number

    # normal division til we reach the largest prime factor of the number
    while num > lowPF:
        if num%lowPF == 0:
            num = num / lowPF
        else:
            lowPF = lowPF + 1

    # Output
    return(f"p003 Ans : {lowPF}")
        
