denom = 1
nom = 1

for i in range(1,11):
    for j in range(1, i + 1):
        for k in range(1, j):
            if((k * 10 + i) * j == k * (i * 10 + j)):
                denom *= j
                nom *= k

print (nom , denom)
print("P033 Answer is: ", denom/nom)