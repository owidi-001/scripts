# import math
# print(math.sqrt(3))

# number=int(input('Enter a square to find it\'s root: '))
# for root in range(number):
#     if number/root == root:
#         print(root)



# MIT RECEIPEE
import random

x=int(input('Enter a number to find the root: '))

g=random.randint(1,x)
# print(g)
while g**2 is not x:
    g=(g+(x/g))/2
    if g**2 == x:
        print('The square root of ',x, ' is ',g)
        break

