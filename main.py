from src.operations import add,subtract,Scalar_Multiplication

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

print(add(A, B))
print(subtract(A, B))
print(Scalar_Multiplication(3, B))
print(Scalar_Multiplication(-3, B))
print(Scalar_Multiplication('hass', B))
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

