"""Arrays

convert list to numpy array and turn it to float 
"""


import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    np_arr = numpy.array(arr,float)
    np_arr = np_arr[::-1]
    return np_arr

arr = input('Enter float or integers seperated by space : ').strip().split(' ')
result = arrays(arr)
print(result)