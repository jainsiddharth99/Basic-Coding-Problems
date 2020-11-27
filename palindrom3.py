def palin(s): 
    if len(s)<=1:
        return True
    else:
        if s[0]==s[-1]:
            return palin(s[1:-1])
        else:
            return False
a=str('malayalam')
if palin(a)==True:
    print('yes')
else:
    print('nope')