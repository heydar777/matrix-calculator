from src.validation import is_valid_matrix,have_same_dimension,can_multiply,is_matrix_2x2,is_square_matrix,is_matrix_3x3


def add(matrix1,matrix2):

    if not is_valid_matrix(matrix1):
        return False
    if not is_valid_matrix(matrix2):
        return False
    
    if not have_same_dimension(matrix1,matrix2):
        return False
    

    result = []

    for i in range(len(matrix1)):

        row = []

        for j in range(len(matrix1[0])):

            row.append(matrix1[i][j] + matrix2[i][j])
        
        result.append(row)
    return result

from src.validation import is_valid_matrix,have_same_dimension


def subtract(matrix1,matrix2):

    if not is_valid_matrix(matrix1):
        return False
    if not is_valid_matrix(matrix2):
        return False
    
    if not have_same_dimension(matrix1,matrix2):
        return False
    

    result = []

    for i in range(len(matrix1)):

        row = []

        for j in range(len(matrix1[0])):

            row.append(matrix1[i][j] - matrix2[i][j])
        
        result.append(row)
    return result


def Scalar_Multiplication(num,matrix):

    if not is_valid_matrix(matrix):
        return False
    if not isinstance(num,int):
        return False

    result = []

    for i in range(len(matrix)):
        row = []

        for j in range(len(matrix[0])):

            row.append(matrix[i][j] * num)

        result.append(row)
    return result

def multiply(matrix1,matrix2):

    if not is_valid_matrix(matrix1):
        return False
    if not is_valid_matrix(matrix2):
        return False

    if not can_multiply(matrix1,matrix2):
        return False
    
    result = []

    for i in range(len(matrix1)):
        row = []

        for j in range(len(matrix2[0])):

            total = 0

            for k in range(len(matrix2)):

                total += matrix1[i][k] * matrix2[k][j]
            
            row.append(total)
        
        result.append(row)
    
    return result

def transpose(matrix):

    if not is_valid_matrix(matrix):
        return False
    
    result = []

    for i in range(len(matrix[0])):

        row = []

        for j in range(len(matrix)):


            row.append(matrix[j][i])
        result.append(row)
    return result

def zeros(rows, cols):

    result = []

    for i in range(rows):
        
        row = []
        
        for j in range(cols):
            
            row.append(0)
        
        result.append(row)
    
    return result

def identity(size:int) -> list:
    """
    Create an identity matrix.

    Args:
        size (int): Number of rows and columns.

    Returns:
        list: Identity matrix.
    """

    if not isinstance(size,int):
        return False

    if size <= 0 :
        return False

    result = []

    for i in range(size):

        row = []

        for j in range(size):

            if i == j :
                
                row.append(1)
            else :
                row.append(0)
        result.append(row)
    
    return result

def determinant_2x2(matrix):

    if not is_valid_matrix(matrix):
        return False
    if not is_matrix_2x2(matrix):
        return False
    
    result = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    

    return result

def minor(matrix,row,col):

    """
    Return the minor matrix after removing
    the specified row and column.
    """

    if not is_valid_matrix(matrix):
        return False
    if not is_square_matrix(matrix):
        return False
    
    if row < 0 or row >= len(matrix):
        return False

    if col < 0 or col >= len(matrix[0]):
        return False
    
    result = []
    for i in range(len(matrix)):
         
        if i == row:
            continue
        new_row = []

        for j in range(len(matrix[0])):
            
            if j == col:
                continue
            new_row.append(matrix[i][j])
        
        result.append(new_row)
    return result


def determinant(matrix):
    
    if not is_square_matrix(matrix):
        return False

    if len(matrix) == 1:
        return matrix[0][0]
    
    if is_matrix_2x2(matrix):
        return determinant_2x2(matrix)
    

    det = 0
    for j in range(len(matrix[0])):

        M = minor(matrix,0,j)
        sign = (-1) ** j
        value = matrix[0][j]
        
        det += determinant(M)*value*sign 
    return det

def cofactor(matrix):

    if not is_valid_matrix(matrix):
        return False

    result = []

    for i in range(len(matrix)):
        row = []

        for j in range(len(matrix[0])):

            sign = (-1) ** (i+j)
            M = minor(matrix,i,j)

            row.append(sign * determinant(M))
        result.append(row)
    return result

def adjoint(matrix):

    if not is_square_matrix(matrix):
        return False

    return transpose(cofactor(matrix))

