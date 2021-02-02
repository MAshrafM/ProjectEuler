perm = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #permutation numbers

limit = 1000000 #iteration limit
permlen = len(perm) #lenght of perm number
cnt = 1 #count

# simple swap function
def swap(i, j):
    temp = perm[i]
    perm[i] = perm[j]
    perm[j] = temp

#iteration to form the permutation    
while(cnt < limit):
    idx = permlen - 1
    
    while(perm[idx - 1] >= perm[idx]):
        idx = idx - 1

    jdx = permlen
    while(perm[jdx - 1] <= perm[idx - 1]):
        
        jdx = jdx - 1

    swap(idx - 1, jdx - 1)

    idx = idx + 1
    jdx = permlen
    while(idx < jdx):
        swap(idx - 1, jdx - 1)
        idx = idx + 1
        jdx = jdx - 1

    cnt = cnt + 1

print(perm)


