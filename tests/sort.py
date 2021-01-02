ol= [64,435, 54, 342,23, 31, 423, 656]
print(dir(ol))
flag=0
# try reverse()
for element in ol:
    k,v=ol[flag],ol[flag+1]
    if k > v:
        ol[k]
        flag+=1
    else:
        continue
