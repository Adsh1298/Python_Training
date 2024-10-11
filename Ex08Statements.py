
age = int(input('Enter your age: '))

if age >= 60:
    print('You are too old to sign up.')
elif age >= 18:
    print('You are now signed up.')
elif age < 0:
    print('You are not even born')
else:
    print('You must be 18+ to sign up')


num, a, b = 5, 6, 7
print('Positive' if num > 0 else 'Negative')
print('Even' if num%2==0 else 'Odd')

#Get the max and min value from the 2 variables in a single line for each iteration
max_num = a if a > b else b
min_num = a if a < b else b
print(f'{max_num} and {min_num}')


