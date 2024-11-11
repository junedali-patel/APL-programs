import numpy as np

arr= np.array([[1,2,3],[2,4,4]])
print (arr)
print(type(arr))
print (arr.shape)
print(arr.ndim)
print(arr.size)

n= np.array([1,2,3,4,5,6,7,8,9,10,11,12])
new_arr=arr.reshape(4,3)
print(new_arr)

