from runners.helpful_fn import Perm

def check(n):   
    s = str(n)
    return int(s[1:4]) % 2 == 0 and int(s[2:5]) % 3 == 0

def p043(): 
    s = 0
    for i in range(0, 18):
        a = int(Perm(i, '4310') + '952867')
        if check(a):
            print(a)
            s += a
        a = int(Perm(i, '6410') + '357289')
        if check(a):
            print(a)
            s += a

    return(f"p043 Ans: {s}")