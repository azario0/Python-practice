"""Arrays

convert lis to arrays and float it
"""


import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    np_arr = numpy.array(arr,float)
    np_arr = np_arr[::-1]
    return np_arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)