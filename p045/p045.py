from runners.helpful_fn import CheckPentagonal

def p045():
    print("Triangular, pentagonal, and hexagonal")
    idx = 143
    flag = True
    while (flag):
        idx += 1
        Hn = idx * (2*idx - 1)
        if(CheckPentagonal(Hn)):
            flag = False

    return(f"p045 Ans: {Hn}")