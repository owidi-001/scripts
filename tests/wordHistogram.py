counts=dict()

try:
    file=input('Enter a file name:')
    if len(file) < 1: file = 'input.txt'
    handle=open(file,'r')
    words=handle.read().split()
    # print(words)
    for word in words:
        counts[word]=counts.get(word,0)+1
    # print(counts)


    bigword=None
    bigcount=None
    # sorting the keys in alphabecical order before calling with the sorted() function
    for word,count in sorted(counts.items()):
        if bigcount is None or count > bigcount:
            bigword=word
            bigcount=count
    print(bigword,bigcount)


except IOError:
    print('File not found')