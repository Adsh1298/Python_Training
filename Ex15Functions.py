def simple_func():
    print('Hello func')

simple_func()

def add_func():
    first_value = float(input('Enter the first value: '))
    second_value = float(input('Enter the second value: '))
    result = first_value + second_value
    print('The added value is: ' + str(result))

def sub_func():
    first_value = float(input('Enter the first value: '))
    second_value = float(input('Enter the second value: '))
    result = first_value - second_value
    print('The added value is: ' + str(result))

def mul_func():
    first_value = float(input('Enter the first value: '))
    second_value = float(input('Enter the second value: '))
    result = first_value * second_value
    print('The added value is: ' + str(result))

def div_func():
    first_value = float(input('Enter the first value: '))
    second_value = float(input('Enter the second value: '))
    result = first_value / second_value
    print('The added value is: ' + str(result))


operation = input('Select a Math Operation: (A)dd, (S)ubtract, (M)ultiply or (D)ivide: ')
# if operation.upper() == 'A':
#     add_func()
# elif operation.upper() == 'S':
#     sub_func()
# elif operation.upper() == 'M':
#     mul_func()
# elif operation.upper() == 'D':
#     div_func()
# else:
#     print('Invalid Operation')
match operation.upper():
    case 'A': add_func()
    case 'S': sub_func()
    case 'M': mul_func()
    case 'D': div_func()
    case _: print('Invalid Operation')