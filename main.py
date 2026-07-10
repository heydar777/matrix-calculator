from src.operations import add,subtract,Scalar_Multiplication,multiply,transpose,zeros,identity,determinant_2x2,minor,determinant
from src.validation import is_matrix_2x2

A = [
    [1,2,3],
    [0 , 1 , 1]
]


B = [
    [1, 2],
    [3, 4]
]

C = [[1,1,1,0],[2,1,4,1],[0,0,9,3],[1,2,1,5]]
print(is_matrix_2x2(A))
print(is_matrix_2x2(B))
print(minor(C,0,0))
print(minor(C,2,0))
print(minor(C,0,1))
print(determinant(C))

