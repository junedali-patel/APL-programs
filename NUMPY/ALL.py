import numpy as np

arr= np.array([[1,2,3],[2,4,4]])
print("FUNCTION  OF Numpy")
print (arr)
print(type(arr))
print (arr.shape)
print(arr.ndim)
print(arr.size)

arr_3d=np.array([[[1,3,4],[1,2,3]],[[2,3,4],[6,7,8]]])
print(arr_3d)
print(arr_3d[0,1,2])
print(arr_3d[1,1,2])
print(arr_3d[1,1,2])


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
sum_arr = a + b

print("Arthimatics of array")
print("SUM" ,sum_arr)
print("SUB" ,a-b)
print("MULTI", a*b)
print("Div" , a/b)


matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[3, 4], [4, 5]])
print("Matrix ")
product_matrix = np.dot(matrix_a, matrix_b)
transpose_a=np.transpose(matrix_a)
transpose_b=np.transpose(matrix_b)
print("Transpose_Matrix A",transpose_a)
print("Transpose_Matrix B",transpose_b)
print ("Matrix add",matrix_a+matrix_b)
print ("Matrix sub",matrix_a-matrix_b)
print("Matrix Product",product_matrix)




n= np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print("Reshape of Numpy")
new_arr = n.reshape((4,3))
print(new_arr)

a1 = np.array([1, 2, 3, 4, 5])
mean_value = np.mean(a1)
standard_deviation=np.std(a1)
min=np.min(a1)
max=np.max(a1)


import numpy as np


arr = np.array([[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], 
                 [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]])

print(arr)
print(arr.shape)