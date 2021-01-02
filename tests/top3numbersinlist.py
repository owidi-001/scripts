# sorting a list 
numbers=[10,20,90,54,67,23,13,45,68,5,7]
big_numbers=[]
for num in numbers:
     count=0
     while count < len(numbers):
             big_numbers.append(max(numbers))
             numbers.remove(max(numbers))
             count+=1
print(big_numbers)

# getting top big numbers in a list
numbers=[10,20,90,54,67,23,13,45,68,5,7]
big_numbers=[]
count=0
while count <3:
        big_numbers.append(max(numbers))
        numbers.remove(max(numbers))
        count+=1
print(big_numbers)