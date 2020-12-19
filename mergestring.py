from statistics import median
str1='abcd'
str2='efgh'
a=''.join([str1, str2])
print(a)
print(a.replace('a',''))


st=[1,2,3,4,5,6,7,8,9]
b=median(st)
print(b)


ar1=[-5,3,6,12,15]
ar2=[-12,-10,-6,-3,4,10]

merge=ar1+ar2
merge.sort()
print(merge)
print('median is',median(merge))
