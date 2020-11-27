def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
    
num=int(input('factorial of: '))
 

if num<0:
    print ('incorrect input')
elif num==0:
    print ('factorial of', num ,'is 1')
else:
    print(factorial(num)) 