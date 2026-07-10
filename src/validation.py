def is_valid_matrix(matrix):
    """
    Check if the input is a valid matrix.

    Rules:
    - Matrix must be a list.
    - Matrix must not be empty.
    - Every row must be a list.
    - Rows must not be empty.
    - All rows must have the same number of columns.
    - Elements must be int or float.
    - Boolean values are not allowed.
    """
    if not isinstance(matrix,list):
        return False
    
    if len(matrix) == 0:
        return False

    if not isinstance(matrix[0],list):
        return False
    if len(matrix[0]) == 0:
        return False
    
    columns_count = len(matrix[0])

    for row in matrix:
        
        if not isinstance(row,list):
            return False
        
        if len(row) == 0:
            return False
        
        if columns_count != len(row):
            return False

        for value in row:

            if isinstance(value,bool):
                return False
            
            if not isinstance(value,(int,float)):
                return False
    return True

def have_same_dimension(matrix1,matrix2):

    """
    Check if two matrices have the same dimensions.
    """

    if not is_valid_matrix(matrix1):
        return False

    if not is_valid_matrix(matrix2):
        return False

    if len(matrix1) != len(matrix2):
        return False
    
    if len(matrix1[0]) != len(matrix2[0]):
        return False
    return True

def is_square_matrix(matrix):

    """
    Check if a matrix is square.
    """

    if not is_valid_matrix(matrix):
        return False
    
    if len(matrix) != len(matrix[0]):
        return False
    
    return True

def is_matrix_2x2(matrix):

    if not is_valid_matrix(matrix):
        return False
    if not is_square_matrix(matrix):
        return False
    
    if len(matrix) != 2:
        return False
    if len(matrix[0]) != 2: 
        return False
    
    return True

def is_matrix_3x3(matrix):

    if not is_valid_matrix(matrix):
        return False
    if not is_square_matrix(matrix):
        return False
    
    if len(matrix) != 3:
        return False
    if len(matrix[0]) != 3:
        return False
    
    return True

def can_multiply(matrix1,matrix2):

    if not is_valid_matrix(matrix1):
        return False

    if not is_valid_matrix(matrix2):
        return False

    return len(matrix1[0]) == len(matrix2)

