vowels=['a','e','i','o','u']
found=[]
word=input('word: ')
for i in word:
    if i not in vowels:
        found.append(i)

print(found)
print(len(found))