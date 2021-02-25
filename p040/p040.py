def p040():
    print("Champernowne's constant")
    s = ""
    for i in range(0, 1000000):
        s += str(i)

    product = 1
    for i in range(0, 7):
        product *= int(s[pow(10,i)])
        print(f"{pow(10,i)} \t {s[pow(10,i)]}")
        

    return(f"p040 Ans : {product}")
