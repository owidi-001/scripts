''':cvar
strings can be compared
the upper case initials are 'smaller' than the lower case initials
'''
# eg
'Owidi' < 'owidi'  # returns True
'Owidi' > 'owidi'  # returns False
'Owidi' == 'owidi'  # returns False

'''
Python has many built in string funtions and can be accessed via: dir(string object)
'''
# name='Owidi'
# print(type(name))
# print(dir(name))

file = open('stringFunctions.txt', 'r')
strFunctions = file.read().split(',')

for func in strFunctions:
    print(func)
