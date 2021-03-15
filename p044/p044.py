from runners.helpful_fn import CheckPentagonal

def p044():
    print("Pentagon numbers")
    flag = True
    D = 0
    idx = 1
    while (flag):
        idx += 1
        Pn = (3*idx - 1)*idx/2
        for jdx in range(idx-1, 0, -1):
            Pm = (3*jdx - 1)*jdx/2
            if(CheckPentagonal(Pn-Pm) and CheckPentagonal(Pn+Pm)):
                D = Pn - Pm
                flag = False
                break
                
    print ("The Pair are: ", Pn, ", ", Pm, "\t The Difference: ", D)
    return(f"p044 Ans: {D}")