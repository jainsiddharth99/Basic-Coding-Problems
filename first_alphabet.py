def firstAlphabet(s):
    ly=""
    word=s.split()
    for i in word:
        ly+=(i[0])
    print(ly)
sentence= 'geeks for geeks'
firstAlphabet(sentence)