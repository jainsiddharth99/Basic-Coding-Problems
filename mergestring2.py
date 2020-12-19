ar1=[-5,3,6,12,15]
ar2=[-12,-10,-6,-3,4]


n=len(ar1)+len(ar2)

ar1.extend(ar2)
ar1.sort()
if  n%2==0:
    median=ar1[int(n/2)]+ar1[int((n/2)+1)]
    print (median)
    
else:
    median=ar1[int(n/2)]
    print (median)