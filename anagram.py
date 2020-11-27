word1=input('word 1: ')
word2=input('word 2: ')

if sorted(word1)==sorted(word2):
    print('string are anagrams')
else:
    print('no they are not anagrams')