class Person:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def display_details(self):
        print(f'The name is {self.name} is from {self.address} and can be contacted by '
              f'{self.phone}')

person = Person(name='Adarsh', phone=8796541230, address='Delhi')
person.display_details()
print('The name of the person is: ' + person.name)


#######################Create Private members in Python###################################
class Student:
    def __init__(self, name, dob):
        self.__name = name
        self.__dob = dob

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

new_student = Student('Adarsh', '1/1/2000')
new_student2 = Student('Anand', '2/2/2000')

print(f'The name is {new_student.get_name()} and his Date of birth is {new_student.get_dob()}')
print(f'The name is {new_student2.get_name()} and his Date of birth is {new_student2.get_dob()}')

