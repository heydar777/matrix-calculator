from src.operations import *



def test_add_2x2():

    A = [
        [1,2],
        [3,4]
    ]

    B = [
        [5,6],
        [7,8]
    ]

    expected = [
        [6,8],
        [10,12]
    ]

    assert add(A,B) == expected

def test_add_negative():

    A = [
        [-1,-2],
        [-3,-4]
    ]

    B = [
        [1,2],
        [3,4]
    ]

    expected = [
        [0,0],
        [0,0]
    ]

    assert add(A,B) == expected

def test_add_invalid_dimension():

    A = [
        [1,2]
    ]

    B = [
        [1,2],
        [3,4]
    ]

    assert add(A,B) == False

def test_subtract():

    A = [
        [5,5],
        [5,5]
    ]

    B = [
        [2,2],
        [2,2]
    ]

    expected = [
        [3,3],
        [3,3]
    ]

    assert subtract(A,B) == expected

def test_scalar_multiply():

    A = [
        [1,2],
        [3,4]
    ]

    expected = [
        [2,4],
        [6,8]
    ]

    assert scalar_multiplication(A,2) == expected

def test_scalar_divide():

    A = [
        [2,4],
        [6,8]
    ]

    expected = [
        [1,2],
        [3,4]
    ]

    assert scalar_divide(A,2) == expected

def test_transpose():

    A = [
        [1,2,3],
        [4,5,6]
    ]

    expected = [
        [1,4],
        [2,5],
        [3,6]
    ]

    assert transpose(A) == expected

def test_identity():

    expected = [
        [1,0,0],
        [0,1,0],
        [0,0,1]
    ]

    assert identity(3) == expected

def test_zero_matrix():

    expected = [
        [0,0],
        [0,0]
    ]

    assert zeros(2,2) == expected

def test_multiply():

    A = [
        [1,2],
        [3,4]
    ]

    B = [
        [5,6],
        [7,8]
    ]

    expected = [
        [19,22],
        [43,50]
    ]

    assert multiply(A,B) == expected

def test_multiply():

    A = [
        [1,2],
        [3,4]
    ]

    B = [
        [5,6],
        [7,8]
    ]

    expected = [
        [19,22],
        [43,50]
    ]

    assert multiply(A,B) == expected

def test_multiply():

    A = [
        [1,2],
        [3,4]
    ]

    B = [
        [5,6],
        [7,8]
    ]

    expected = [
        [19,22],
        [43,50]
    ]

    assert multiply(A,B) == expected