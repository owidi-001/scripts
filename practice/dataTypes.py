# numeric (integers, complex numbers, floats)
i=50
j=40.5
c = i+3j
print(type(i))
print(type(j))
print("The type of c", type(c))
print(" c is a complex number", isinstance(i+3j,complex))

# sequence types(string,list and tuple)
# string
a='string is between quotes'
print('hellow' + 'world')
print('''this is 
a multy line string''')
print(type(a))
print(a[-2])
print(a[0:2])
print(a*2)

# list
b=['meat',45,12.3,'mango','head']
b[4]='ongea'
print(type(b))
print(b)
print(b[:2])
print(b[3:])

# tuple
yup=('hi',20,'learning python')
print(type(yup))
print(yup)

# dictionary
books={
    'Ken':'Kidagaa',
    'margret':'The river',
    'Moses':'Bible'
}
print(books)
print(type(books))
print(books.keys())
print(books.values())


# booleans
print(type(True))
print(type(False))


# set(mutable,
z={'diseases',2020,'corona virus','lockdown',21}
print(z)
print(type(z))
z.add(1998)
z.remove(2020)
print(z)






