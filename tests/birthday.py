import time
from datetime import date

birthday = input('Enter date of birth in the format: YYYY-MM-DD :')
dob = birthday.split('-')

birthdate = date(int(dob[0]), int(dob[1]), int(dob[2]))

age = date.today() - birthdate
print(age)
print(age/365 ,'Years old')
