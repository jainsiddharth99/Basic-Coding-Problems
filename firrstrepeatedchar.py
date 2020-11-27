word='bbilling'
list=[]
def first_repeated(word):
    for char in word:
        if char in list:
            print(char)
            break
        else:
            list.append(char)
            
first_repeated(word)
        
list2=[] 
count={}
       
def firstnonrepeate(word):
    for char in word:
        if char not in list2:
            count.setdefault(char,0)
            count[char]+=1
        else:
            list2.append(char)
    for char in count:
        if count[char]==1:
            return char
    
            
print(firstnonrepeate(word))
    
