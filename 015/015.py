"""
    Problem 15
    Lattice paths
"""

grid_length = 20 # Given Grid Length
path = 1  # Path holder

# Loop possible routes
# wiki: http://en.wikipedia.org/wiki/Binomial_coefficient
# using binomial coefficient
for idx in range(0, grid_length):
    path = (path * (grid_length * 2 - idx)/(idx+1))

# Output
print ('p015 Ans: ', path)
