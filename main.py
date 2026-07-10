from src.operations import add,subtract,Scalar_Multiplication,multiply,transpose,zeros,identity,determinant_2x2,minor,determinant,cofactor
from src.validation import is_matrix_2x2

A = [
    [1,2,3],
    [0 , 1 , 1]
]


B = [
    [1, 2],
    [3, 4]
]
A = [[1,2,3],[1,0,1],[1,2,2]]
C = [[1,1,1,0],[2,1,4,1],[0,0,9,3],[1,2,1,5]]

print(minor(C,0,0))
print(minor(C,2,0))
print(minor(C,0,1))
print(determinant(C))
print(cofactor(A))
print(cofactor(C))