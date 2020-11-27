def palindrome(word):
    return word==word[::-1]
        
word=input('word: ')
ans=palindrome(word)
if ans:
    print('YES')
else:
    print('no')
    
def simple_palindrome(word_1):
    if word==word[::-1]:
        print('yes it is palindrome')
    else:
        print('no it is not')
s='geeeeg'
print(simple_palindrome(s))    