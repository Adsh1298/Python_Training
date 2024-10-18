class Student:
    count = 0 # class members
    total_gpa = 0.0
    def __init__(self, name, gpa):
        self.student_name = name
        self.student_gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_student_info(self):
        return f'{self.student_name} {self.student_gpa}'

    @classmethod
    def get_count(cls):
        return f'Total no of students are {cls.count}'

    @classmethod
    def get_all_gpa(cls):
        return f'Total GPA is {cls.total_gpa}'

    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f'Average GPA: {cls.total_gpa / cls.count}'

s1 = Student('Phaniraj', 6.8)
print(s1.get_student_info())
s2 = Student('Ramesh', 7.8)
print(s2.get_student_info())
s3 = Student('Adhithya', 9.8)

print(s3.get_student_info())
s4 = Student('Adarsh', 5.8)
print(s4.get_student_info())

print(Student.get_count())
print(Student.get_all_gpa())
print(Student.get_avg_gpa())