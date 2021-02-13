def is_palindromic(n): return str(n)==str(n)[::-1]

limit = 1000000

result = 0

for i in range(1, limit, 2):
    base2= int(bin(i)[2:])
    if(is_palindromic(i) and is_palindromic(base2)):
        print(i, " >> ", base2)
        result += i

print (result)
