from src.operations import add,subtract,Scalar_Multiplication,multiply,transpose,zeros

A = [
    [1,2,3],
    [0 , 1 , 1]
]

B = [
    [1, 1],
    [2, 0],
    [0, 1]
]

print(transpose(A))
print(transpose(B))
print(zeros(2,3))
print(zeros(4,3))
A = [
    [1, 2],
    [3]
]

B = [
    [1, 2],
    [3, 4]
]
print(Scalar_Multiplication(3, A))
print(add(A, B))
print(subtract(A, B))

