sum = 0 # Sum Variable

# Number below a 1000
for idx in range(1000):
  #multiple of 3 or 5
  if (idx % 3 == 0 or idx % 5 == 0):
    sum += idx

# Output 
print("p001 Ans: ", sum)
