def get_determinate(matrix):
    # Told to assume that matrix is always square, non empty
    n = len(matrix[0])
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    
    det = 0
    for i in range(n):
        top = matrix[0][i]
        rest_matrix = []
        for row in range(n):
            if row == 0:
                continue
            rest_row = []
            for col in range(n):
                if col == i:
                    continue
                rest_row.append(matrix[row][col])
            rest_matrix.append(rest_row)
        

        rest_matrix_det = get_determinate(rest_matrix)
        pattern = top * rest_matrix_det
        # all odd values are negative
        if i % 2 == 1:
            pattern = pattern * -1
        det += pattern
    return det