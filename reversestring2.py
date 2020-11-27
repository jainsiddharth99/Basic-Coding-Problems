
def reverse(s): 
    str = "" 
    for i in s: 
        # here str=i+str means all elements in s are added in way
        # where we add elements in the beginning
        # so first g is inserted, than e, then e, thek k .......
        #if it was str +i then elemnt is added in back
	    str =i+str
    return str

s = "Geeksforgeeks"

print ("The original string is : ",end="") 
print (s) 

print ("The reversed string(using loops) is : ",end="") 
print (reverse(s)) 

def recursive_reverse(s):
    if len(s)==0:
        return s
    else: 
        return recursive_reverse(s[1:])+s[0]
    
s = "Geeksforgeeks"

print ("The original string is : ",end="") 
print (s) 

print ("The reversed string(using loops) is : ",end="") 
print (recursive_reverse(s)) 