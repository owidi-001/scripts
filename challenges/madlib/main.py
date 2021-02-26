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
    try:
        substitutes=input('Enter a sentence to use as replacement').split(' ')
        file=input('Enter file name: \n')
        story=open(file,'r').read().split(' ')
    except IOError:
        substitutes=['jina','blaah','something','ok','tester']
        story=open('file.txt','r').read().split(' ')

    madLib(story,substitutes)


