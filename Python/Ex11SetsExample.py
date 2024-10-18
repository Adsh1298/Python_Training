names = {'Phani', 'Vinod', 'Banu', 'Ramnath', 'Jaydeep'}
print(names)
print(names)

for name in names:
    print(name)

names.add('Adarsh')
print(names)

last_name = {'Kumar', 'Raj', 'Mahato', 'Pal'}
print(last_name)

names.update(last_name)
print(names)

thisset = {'apple', 'banana', 'cherry'}
thisset.remove('banana')
print(thisset)

thisset.discard('banana')

last_name.pop()
print(last_name)

thisset.clear()
print(thisset)

