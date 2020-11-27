def prime(num,i=2):
    if num<=2:
        return num
    elif num==2:
        return 1
    elif num%i==0:
        return 0
    return prime(num,i+1)

num=int(input('terms:'))
for i in range(num):
    print(prime(num))
