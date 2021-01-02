count=dict()

names=['ten','seven','nine','nine','nine','five','zero','zero','two','three','one','eight']

for name in names:
    count[name]=count.get(name,0)+1
print(count)