max=int(input('Enter your max value: '))

grt=1
for num in range(1,max):
    if num>grt:
        grt=num

for j in range(1,max+1):
    if grt%j==0:
        continue
    else:
        grt*=j
        
print('Your LCM is: ',grt)
            
            
