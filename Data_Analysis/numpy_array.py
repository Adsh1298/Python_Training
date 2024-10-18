import numpy as np
import scipy
#
# #numpy is a python library for performing numerical calculations in python.
# #arrays are the most optimized collection components. Its fixed in size and once the memory is
# # set you can use it to perform various kind of operations.
# arr = np.array([1, 2,3 ,4,5,6,])
# print('Arr: ',arr)
#
# arr2 = np.array([[1,2,3,4], [4,5,6,7]])
# print('Arr2:\n', arr2)
#
# #Adding arrays :
# arr3 = np.array([6,5,4,3,2,1])
# sum_arr = arr + arr3
# print(sum_arr)
# mul_arr = arr * arr3
# print(mul_arr)
#
# avg = np.mean(mul_arr)
# print(avg)
# print('Std Deviation: ', np.std(mul_arr))
#
# print('No of dimensions: ', arr2.ndim)
# print('No of elements: ', arr2.size)
# print()

arr1 = np.array([1,2,3,4,5,1,1,1])
'''
print(np.sqrt(arr1))
print(np.sin(arr1))
print(np.log(arr1))

print(arr1[(arr1 >= 3) & (arr1 <=10)])
'''
'''
mean = np.mean(arr1)
median = np.median(arr1)
std_deviation = np.std(arr1)
variance = np.var(arr1)
mode = stats.mode(arr1)
print(f'Mean:', mean)
print(f'Median: ', median)
print(f'Standard Deviation: ', std_deviation)
print(f'Variance: ', variance)
print(f'Mode: ', mode)
'''
'''
arr1 = np.array([3,4,2,5,1,6,9,8])
sorted_arr = np.sort(arr1)
sorted_indices = np.argsort(arr1)
print(sorted_arr, sorted_indices)
'''

arr1 = np.array([3,4,2,5,5,1,9,9,8])
unique_values = np.unique(arr1, return_counts=True)
unique_counts = np.unique_counts(arr1)
print('Unique values: ', unique_values)
print('Unique count: ', unique_counts)

