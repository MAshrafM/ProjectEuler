List = []

for a in range(2, 101):
    for b in range(2,101):
        result = pow(a,b)
        if result not in List:
            List.append(result)

print (len(List))