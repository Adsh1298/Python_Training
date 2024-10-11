grades = [90, 45, 67, 55, 67, 89, 23, 67]
#passing_grades = list(filter(lambda grade: grade > 60, grades))
#print(passing_grades)
my_grades = {}
for grade in grades:
    x = lambda g: 'pass' if g > 50 else 'fail'
    my_grades[grade] = x
print(my_grades)
for key in my_grades.keys():
    print(f'Grade: {key}, Result: {my_grades[key]}')
# print(pass_fail)
#exercise: even grades and odd grades
even_grades = list(filter(lambda x: x%2==0, grades))
print(even_grades)

for i in grades:
    if i > 60:
        pass_fail[i] = 'Pass'
    else:
        pass_fail[i] = 'Fail'

print(pass_fail)