#Parameters are the way of inserting inputs to the functions. Any variable created in the
# function is limited to the function itself. So any values that you want to send to the Function
# should be sent in the form of argument or parameter.


def add_func(v1, v2):
    return v1 + v2

def sub_func(v1, v2):
    return v1 - v2

def mul_func(v1, v2):
    return v1 * v2

def div_func(v1, v2):
    return v1 / v2

def calculate(v1, v2):
    sum_value = add_func(v1, v2)
    sub_value = sub_func(v1, v2)
    mul_value = mul_func(v1, v2)
    div_value = div_func(v1, v2)
    return sum_value, sub_value, mul_value, div_value

a, s, m, d = calculate(13, 12)
# print(f'The added value is {a}, subtracted value is {s}, multiplied value is {m} and the divided '
#       f'value is {d:.2f}')

##############################
# 4 kinds of parameters: Positional, Default, Keyword, Arbitrary

#Positional parameters
def display_invoice(name, amount, due_date):
    print(f'Hii Mr. {name}')
    print(f'An amount of Rs. {amount} is pending from your end')
    print(f'The last date for your payment is on {due_date}')
    print('Please ignore if already paid !!')
# In this scenario, the position of the parameters shall not change when we pass the parameters
# into the function
display_invoice('Adarsh','12/12/2024',45000 )
###############################################################
#Default Parameters
def get_net_price(list_price, discount = 0, tax = 0.05):
    total_price = list_price * (1 - discount) * (1 + tax)
    return total_price
# Default parameters should not followed by non-default parameters.
print(get_net_price(500, 0.1))
###############################################################
# Keyword parameters: you can precede a parameter with its identifier and place them in any order
def greeting(message, title, name):
    print(f'{message}!!!', end = ' ')
    print(f'{title}', end=' ')
    print(f'{name}')

greeting(title='Mr', message='Good Afternoon', name='Ramesh')

###############################################################
#variable no. of arguments. You can pass multiple values to the function.
def add_numbers(*args):
    total = 0.0
    for arg in args:
        total += arg
    return total
# * is a wild character that implies multiple values.
print(add_numbers(1, 2, 3, 4, 5))

def get_address(**kwargs):
    print(f'{kwargs.get('flat_no')}, {kwargs.get('apartment_name')}')
    print(f'{kwargs.get('area')}, {kwargs.get('pin')}')
# ** is a wild character that implies multiple keyword arguments. Internally they are dictionary
get_address(flat_no=326, area='RR Nager', apartment_name='Vastu hillView 2', city='Banglore',
            pin=560098)