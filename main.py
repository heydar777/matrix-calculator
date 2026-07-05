from src.validation import *

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

C = [
    [1, 2, 3],
    [4, 5, 6]
]

print(is_valid_matrix(A))
print(have_same_dimension(A, B))
print(is_square_matrix(A))
print(can_multiply(A, C))