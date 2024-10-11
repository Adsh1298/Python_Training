# name = 'Adarsh'
#
# print(name)
# print(type(name))

# first_name = 'Adarsh'
# last_name = 'Kumar'
# full_name = '1 ' + first_name + ' ' + last_name
# print(full_name)
# print(f'{2} {first_name} {last_name}')
#
# print(type(full_name))

age = 26
print(age)
print(type(age))
age += 6 # same as 'age = age + 6'
print(age)

print('Your age is: ' + str(age))
print(f'Your age is {age}')

height = 23.45
print(height)
print(type(height))
print('Your Height is ' + str(height) + ' inches')


is_Male = True
print(is_Male)
print(type(is_Male))
print(int(is_Male))

######### Important Points ###########
'''
Multiline Comments
Naming conventions:
lowercase, underscore_between_words,
should not start with numbers.
There is no specific type for numbers and floats. A variable could hold either Python allows extremely large 
values for numericals without loosing any precision strings with  "" or '' are same. Its only a 
matter of convenience.
Bool Value should be True or False and is case sensitive.
All conventions and coding standards are defined by PEP(Python Enhancement Proposals).
Currently it is PEP8
If a variable is declared but not assigned, it is None. In the context of the Boolean it is False.
'''

name, age, attractive = 'Adarsh', 26, True
print(f'{name} is of {age} years and his personality is {attractive}')

phani = rajan = ram = 47
print(f'{phani} {rajan} {ram}')