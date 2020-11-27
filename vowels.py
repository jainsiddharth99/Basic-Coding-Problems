vowels=['a','e','i','o','u']
found=[]
word=input('word: ')
for i in word:
    if i in vowels:
        found.append(i)

print(found)