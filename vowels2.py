vowels=['a','e','i','o','u']
found={}
word=input('word: ')
for i in word:
    if i in vowels:
        found.setdefault(i,0)
        found[i]+=1
        

print(found)