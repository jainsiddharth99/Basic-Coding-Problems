x=int(input("x: "))
y=int(input('y: '))

print('BEFORE:\nvalue of x is',x,'value of y is',y)

# create a temporary variable and assign value of a variable
# here temp hold value of x
temp=x
# now that temp has the value of x we can change the value of x
x=y
# now x is y and temp has the old value of x so now we can give
# that value to y
y=temp

print('AFTER:\nvalue of x is',x,'value of y is',y)