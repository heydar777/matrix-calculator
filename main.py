from src.operations import add,subtract

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
A = [
    [1, 2],
    [3]
]

B = [
    [1, 2],
    [3, 4]
]

print(add(A, B))
print(subtract(A, B))