import numpy as np
from numpy import linalg as la
arr=np.array([[1,0,0],[0,1,0],[0,0,1]])
trace=np.trace(arr)
print("The sum of diagonal elements is",trace)

egien_value=la.eigvals(arr)
print("Eigenvalues of the matrix are",egien_value)
determinant=np.linalg.det(arr)
print("Determinat value of matrix is",determinant)
inverse=np.linalg.inv(arr)
print("Inverse of the matrix is",inverse)

