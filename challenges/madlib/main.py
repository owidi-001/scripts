import random

def madLib(story,substitutes):
    """
    docstring
    """
    count=len(substitutes)

    while count>0:
        num=random.randrange(len(story))
        replace=random.randrange(len(substitutes))
        # confirmation
        # print(story[num],'is replaced by ',substitutes[replace])
        story[num]=substitutes[replace]
        count-=1
    separator=' '
    print(separator.join(story))
    


if __name__ == "__main__":
    substitutes=['jina','blaah','something','ok','tester']

    try:
        file=input('Enter file name: \n')
        story=open(file,'r').read().split(' ')
    except IOError:
        story=open('file.txt','r').read().split(' ')

    madLib(story,substitutes)


