digits=int(input('Enter max digits: \n'))
start=10**(digits-1)
stop=10**digits
max=0

print(start)
print(stop)

for i in range(start,stop):
    for j in range(start,stop):
        product=i*j
        strProd=str(product)
        if strProd==strProd[::-1]:
            int(product)
            if product > max:
                max=product
            
    
print(max)
# product=str(num*start)
#     if product==product[::-1]:
#         print(product)
#     if int(product)>max:
#         max+=int(product)
#     start+=1




