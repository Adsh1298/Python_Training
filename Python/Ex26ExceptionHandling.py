'''
try:
    print(sample)
except NameError:
    print('Variable sample is not defined')
except:
    print('Unknown error occurred')

def div_numbers(a, b):
    try:
        result = a / b
    except (ZeroDivisionError, TypeError) as ex:
        print(f'The error is {ex}')
    # except TypeError:
    #     print('The Data type is invalid')
    except Exception as e:
        print(f'Unknown Exception has occurred: {e}')
    else:
        print(f'Result: {result}')
    finally:
        print('Execution completed')

div_numbers(10,5)
print('###########################')
div_numbers(10, 0)
print('###########################')
div_numbers(5, 'apple')
'''
from tabnanny import check
from xml.dom import ValidationErr


#Raising Exceptions
'''
def check_for_even_number(num):
    if num%2==0:
        return True
    else:
        raise ValueError('Number cannot be odd')

try:
    print(check_for_even_number(11))
except ValueError as e:
    print(f'Exception caught: {e}')
'''
#########Custom Exception##########
# Custom Exceptions in Python are classes derived from Exception, the base class for all kinds of
# Exceptions.
class EmployeeNotFound(Exception):
    def __init__(self, message):
        self.message = message

def find_employee(id):
    if id < 35:
        print(f"Employee found with ID {id}")
    else:
        raise EmployeeNotFound(f"Employee with Id {id} not found!!!!")

try:
    find_employee(46)
except EmployeeNotFound as e:
    print(f"{e}")
else:
    print("Employee found successfully, shall share the details shortly")
finally:
    print("Application exited gracefully")