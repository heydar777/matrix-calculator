from src.validation import *

def test_valid_matrix():

    matrix = [
        [1,2],
        [3,4]
    ]

    assert is_valid_matrix(matrix)

def test_invalid_row_length():

    matrix = [
        [1,2],
        [3]
    ]

    assert not is_valid_matrix(matrix)

def test_empty_matrix():

    assert not is_valid_matrix([])

def test_non_numeric():

    matrix = [
        [1,"A"],
        [3,4]
    ]

    assert not is_valid_matrix(matrix)
def test_boolean():

    matrix = [
        [True,2],
        [3,4]
    ]

    assert not is_valid_matrix(matrix)

def test_float():

    matrix = [
        [1.5,2],
        [3,4]
    ]

    assert is_valid_matrix(matrix)