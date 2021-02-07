result = 0

for i in range(2000, 200000):
    sums = 0
    num = i
    while(num > 0):
        digit = num % 10
        num //= 10

        temp = pow(digit, 5)

        sums += temp
       
              
    if(sums == i):
        result += i
        print("number : ", i,"\t sum of 5th : ", sums)

print(result)