"""
  Problem 14
  Longest Collatz sequence
"""
def p014():
    print("Longest Collatz sequence")
    # Given Limit
    limit = 1000000

    length = 0  # Length of the sequence
    start = 0   # required output, the start of the sequence
    chain = [1, 1]  # sequence chain

    # loop below a million
    for idx in range(2, limit):
        kdx = 0  # sequence length
        index = idx # secondary pointer
        # loop for Collatz sequence
        while(index != 1):
            kdx = kdx + 1
            if(index%2 == 0):
                index = index/2
            else:
                index = 3 * index + 1
        # chain length for iteration       
        chain.append(kdx)
        # checking longest chain
        if(chain[idx] > length):
            length = chain[idx]
            start = idx
    #Output
    return(f"p014 Ans: {start}")

    #PS: This is working but it is not efficient this takes longer than seconds.
