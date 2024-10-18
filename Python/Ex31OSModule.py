#The OS module is used to extract information from the OS where the Application is executing. It
# allows to perform tasks on File and Directory management, environment variables and process
# information.

import os

cur_dir = os.getcwd()
print(f'Currently working in {cur_dir}')

all_details = os.listdir(cur_dir)
for file in all_details:
    print(f'File name: {file}')

#Use environment variables:
path_var = os.environ.get('PATH')
print(f'Environment variable for Path: {path_var}')

#Check if the directory exists:
if os.path.exists(cur_dir):
    print('This directory exists')
else:
    os.mkdir(cur_dir)
    print(f'A new directory {cur_dir} is now created')

print(dir(os))

#Get the list of available drives in OS
lis_drives = os.listdrives()
print(lis_drives)