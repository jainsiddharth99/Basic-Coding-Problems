def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=5
for i in range(n):
    print(fib(i))
    
def factor(n):
    if n==1:
        return n
    else:
        return n*factor(n-1)
    
l=5
print(factor(5))