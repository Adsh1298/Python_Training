import math as m
'''
x = m.pi
print(x)
y = -5.123
z = 5
result = abs(y)
print(result)

result = max(x, y, z)
print(result)

result = pow(5,2)
print(result)

mn = min(x, y, z)
print(mn)

result = m.sqrt(81)
print(result)

result = m.isqrt(10)
print(result)

result = m.perm(8, 5)
print(result)
'''

#Exercise 1: Circumference of cirlce
'''
radius = float(input('Enter radius of the circle: '))
circumference = 2*m.pi*radius
print(f'Circumference of circle: {circumference:.2f}')

#Exercise 2: Area of circle
radius = float(input('Enter radius of the circle: '))
area = m.pi*pow(radius, 2)
print(f'Area of circle: {area:.2f}')
'''

#Exercise 3: Find the hypotenuse of a Triangle:
a = float(input('Enter the length of side A :'))
b = float(input('Enter the length of side B :'))
c = m.sqrt(pow(a, 2) + pow(b,2))
print(f'The Length of side C is {c}')

#Exercises at Home:
#Write a Program to find an area of a Polygon.
#Write a program to print a multiplication table of number.



