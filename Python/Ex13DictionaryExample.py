capitals = {'USA': 'Washington DC', 'India': 'New Delhi', 'China': 'Beijing', 'Japan': 'Tokyo'}
print(capitals)

capitals.update({'Germany':'Berlin'})
print(capitals)

capitals['Cananda'] = 'Ottawa'
capitals['India'] = 'Bhopal'

capitals.pop('China')
print(capitals)

keys = capitals.keys()
print(keys)
values = capitals.values()
print(values)

for key in keys:
    print(f'Country: {key},  Capital: {capitals[key]}')
print('#####################################################')
for key, value in capitals.items():
    print(f'Country: {key}, Capital: {value}')

#Exercise 1: Create a data for an Employee
employee = {}
employee['id'] = 123
employee['name'] = 'Adarsh'
employee['address'] = 'Banglore'
employee['salary'] = 45000

print('These are the details of the Employee: ')
for key, value in employee.items():
    print(f'{key} : {value}')
