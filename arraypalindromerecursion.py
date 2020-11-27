def palin(arr,s,e):
    if s>=e:
        return True
    if arr[s]==arr[e]:
        return palin(arr,s+1,e-1)
    if s!=e:
        return False
    return True

arr=[1,2,3,4,4,3,2,1]
length =len(arr)

if palin(arr,0,length-1):
    print('yes')
else:
    print('no')
        