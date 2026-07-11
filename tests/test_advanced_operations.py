from src.operations import *

def test_minor_3x3():

    A = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    expected = [
        [4,6],
        [7,9]
    ]

    assert minor(A,0,1) == expected
def test_minor_center():

    A = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    expected = [
        [1,3],
        [7,9]
    ]

    assert minor(A,1,1) == expected
def test_minor_invalid():

    A = [
        [1,2],
        [3]
    ]

    assert minor(A,0,0) == False

def test_determinant_2x2():

    A = [
        [1,2],
        [3,4]
    ]

    assert determinant(A) == -2

def test_determinant_3x3():

    A = [
        [1,2,3],
        [0,4,5],
        [1,0,6]
    ]

    assert determinant(A) == 22
def test_determinant_identity():

    A = [
        [1,0,0],
        [0,1,0],
        [0,0,1]
    ]

    assert determinant(A) == 1

def test_determinant_zero():

    A = [
        [1,2],
        [2,4]
    ]

    assert determinant(A) == 0
def test_cofactor_2x2():

    A = [
        [1,2],
        [3,4]
    ]

    expected = [
        [4,-3],
        [-2,1]
    ]

    assert cofactor(A) == expected

def test_cofactor_3x3():

    A = [
        [1,2,3],
        [0,4,5],
        [1,0,6]
    ]

    expected = [
        [24,5,-4],
        [-12,3,2],
        [-2,-5,4]
    ]

    assert cofactor(A) == expected

def test_adjoint():

    A = [
        [1,2],
        [3,4]
    ]

    expected = [
        [4,-2],
        [-3,1]
    ]

    assert adjoint(A) == expected

def test_adjoint():

    A = [
        [1,2],
        [3,4]
    ]

    expected = [
        [4,-2],
        [-3,1]
    ]

    assert adjoint(A) == expected

def test_inverse_not_exist():

    A = [
        [1,2],
        [2,4]
    ]

    assert inverse(A) == False

def test_inverse_identity():

    A = [
        [1,0],
        [0,1]
    ]

    expected = [
        [1,0],
        [0,1]
    ]

    assert inverse(A) == expected

