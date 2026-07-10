from src.operations import add,subtract,Scalar_Multiplication,multiply,transpose,zeros,identity,determinant_2x2
from src.validation import is_matrix_2x2

A = [
    [1,2,3],
    [0 , 1 , 1]
]


B = [
    [1, 2],
    [3, 4]
]
print(is_matrix_2x2(A))
print(is_matrix_2x2(B))
print(determinant_2x2(B))
print(subtract(A, B))

