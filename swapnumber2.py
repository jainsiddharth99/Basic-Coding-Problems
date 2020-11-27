x=10
y=20
z=30
print('BEFORE:\nvalue of x is',x,'value of y is',y,z)

x,y,z=y,z,x

print('AFTER:\nvalue of x is',x,'value of y is',y,z)

a=10
b=20
print('BEFORE:\nvalue of x is',a,'value of y is',b)
a=a+b # here a(10)=a(10)+b(20) so a becomes 30
b=a-b # here a is now 30 but b is still 20 so now after a-b, b =10
# (one value swapped)
a=a-b # here a=a-b makes a 20 ( a(30)-b(10))
# both values swapped

print('AFTER:\nvalue of x is',a,'value of y is',b)