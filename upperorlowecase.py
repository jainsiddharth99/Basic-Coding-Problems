word='Siddharth Jain'
upper=[]
lower=[]
for i in word:
    if i.isupper():
        upper.append(i)
    elif i.islower():
        lower.append(i)
    else:
        pass
for i in upper:
    print(i)
print('number of upper case words: ',len(upper))
    
for i in lower:
    print(i)
print('number of lower case words: ',len(lower))
