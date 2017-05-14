"""
    problem 9
    Special Pythagorean triplet
"""

# min range for the triplets
for idx in range(3, 333):
    for jdx in range(idx + 1, (999-idx)//2):
        # main equation
        c = 1000 - idx - jdx
        # pythagorean
        if(c*c == idx*idx + jdx*jdx):
            # Output
            print("p009 Ans: ", idx*jdx*c)
