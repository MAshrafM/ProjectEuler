from runners.helpful_fn import CheckPandigital

def p032():
    print("Pandigital products")
    p = set()   
    for i in range(2, 80):
        start = 1234 if i < 10 else 123 
        for j in range(start, 10000//i):
            # check the mulipand the muliplier and the product
            if CheckPandigital(str(i) + str(j) + str(i*j)):
                p.add(i*j)
    print(f"the pandigital numbers: {p}")
    return(f"p032 Ans: {sum(p)}")