#DateTime module in python contains classes for working with Date and Time. With these APIs,
# you can perform operations on Date and Time extracting the System Date and Time, performing
# mathematical operations on Date and Time.

import datetime as dt
from datetime import datetime

#current datetime
now = dt.datetime.now()
print(str(now))

#current time
time = now.strftime('%H:%M:%S')
print(time)

time = f'{now.time().hour}:{now.time().minute}:{now.time().second}'
print(time)

#current date
date = dt.datetime.today()
date = now.strftime('%Y-%m-%d')
print(date)

#How about taking inputs from the user ?
# dob = input('Enter the Date of Birth')
# date_of_birth =dt.datetime.strptime(dob, '%d-%m-%Y')
# print(date_of_birth)

#Todo: Calculate the age base on the date of birth:
def calculate_age(dateofbirth):
    #Get Today's date
    today = dt.datetime.today()
    age = today.year - dateofbirth.year
    if(today.month, today.day) < (dateofbirth.month, dateofbirth.day):
        age -= 1
    return age

dob = datetime(1976, 12, 1)
age = calculate_age(dob)
print(age)

#Adding Date
my_retirement_year = now.year + 4
print(f'The selected date is {my_retirement_year}')

#adding days
my_retirement_date = now + dt2.timedelta(days=100)
print(f'{my_retirement_date}')

#subtract the days:
previous_visit = now - dt.date(2023, 5, 1)
print(previous_visit)

#################Importnt Points######################
"""
datetime.datetime.now: Gets the system date and time
datetime.datetime.today: returns the current system date
strftime() is used for formatting the date time
strptime() is used to parse the string to a valid datetime
timedelta() is used to add/subtract dates
"""