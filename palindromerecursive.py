def palindrome(string,s,e):
    if s==e:
        return True
    if string[s]!=string[e]:
        return False
    if s<e+1 :
        return palindrome(string,s+1,e-1)
    return True

word=input('word: ')
n=len(word)
if palindrome(word,0,n-1):
    print('yes')
else: 
    print('no')
    
    
