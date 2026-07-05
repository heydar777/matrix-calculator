from src.validation import is_valid_matrix,have_same_dimension


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

        for j in range(len(matrix1)):

            row.append(matrix1[i][j] + matrix2[i][j])
        
        result.append(row)
    return result
