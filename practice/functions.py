import random

def checkMatch(data,target):
    if target==data:
        return True
    return False


if __name__=='__main__':
    data=random.randrange(0,100)
    target=eval(input('What\'s your guess:'))
    if checkMatch(data, target):
        print("Success")
    else:
        print(f'Naah it was {data} try again')