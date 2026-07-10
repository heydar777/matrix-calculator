from src.validation import is_valid_matrix,have_same_dimension,can_multiply


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


