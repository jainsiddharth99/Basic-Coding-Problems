terms=int(input('num of terms: '))
num1=0
num2=1

if terms <= 0:
    print('incorrect input')
elif terms==1:
    print(num1)
elif terms==2:
    print(num2)
else:
    print('fibonaaci sequence:')
    
    for i in range(terms):
        i=num1+num2
        num1=num2
        num2=i
        
        print(i)
        
        
        
