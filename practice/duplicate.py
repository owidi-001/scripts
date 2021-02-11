numbers=list()
newNums=list()

try:
    print('Enter numbers')
    while True:
        entry=int(input(''))
        numbers.append(entry)
except:
    print(numbers)

for num in numbers:
    if num not in newNums:
        newNums.append(num)

print(newNums)