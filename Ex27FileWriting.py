#File reading writing is done using the built-in global methods
'''
w - writing, overwrites if the file exits
r - reading mode, default mode
a - append mode, Appends the file and the data is added at the end of the file
x - exclusive creation, creates a new file and writes to it, if the file exists raises an Exception
t - text mode, opening the file as text file
+ - wild character for both reading and writing
'''
################################Writing a text file ###############################
file_name = 'SampleFile.txt'
try:
    with open(file_name, 'x') as file:
        file.write('Hello World from Python into a file')
        print(f'.txt file {file_name} has been created successfully.')

except FileNotFoundError as err:
    print(f'Error Details: {err}')

except Exception as genEx:
    print(f'Unknown error: {genEx}')

##############Writing JSON Data#########################
#JSON: JavaScript Object Notation
import json
empRecord = [{
    'empId': 123,
    'empName': 'Phaniraj',
    'empAddress':'Banglore',
    'salalry': 45000
},
    {
    'empId': 124,
    'empName': 'Adarsh',
    'empAddress':'Delhi',
    'salalry': 48000
    }
]

file_name = 'empRecords.json'
try:
    with open(file_name, 'w') as file:
        json.dump(empRecord, file, indent=8)
        print(f'JSON data stored successfully')
except FileExistsError as err:
    print(f'{err}')

##############Converting a List of EMployees to JSON Data##########
class Customer:
    def __init__(self, name, address, bill):
        self.cstname = name
        self.address = address
        self.bill = bill

    def to_dict(self):
        return {'cstname': self.cstname, 'address': self.address, 'bill': self.bill}

def writeJsonFile(jsondata, fileName):
    try:
        with open(fileName, 'w') as file:
            json.dump(jsondata, file, indent=3)
    except:
        print(f'{e}')

customers = [Customer('Phaniraj', 'Banglore', 4000),
             Customer('Phaniraj', 'Banglore', 4000),
             Customer('Phaniraj', 'Banglore', 4000),
             Customer('Phaniraj', 'Banglore', 4000)]

jsonObjects = [cst.to_dict() for cst in customers]

json_data = json.dumps(jsonObjects)

writeJsonFile(jsonObjects, "Customers.json")
