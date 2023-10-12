import numpy as np


def i_j_minor(matrix, i, j):
    mat = [row[:j] + row[j + 1:] for row in matrix[:i] + matrix[i + 1:]]
    return mat


def choose_row(matrix):
    best_row = 0
    min_nonzeroes = len(matrix[0])
    for row_id, row in enumerate(matrix):
        count_nonzeroes = sum(1 for element in row if element != 0)
        if count_nonzeroes < min_nonzeroes:
            min_nonzeroes = count_nonzeroes
            best_row = row_id
    return best_row


def determinant_of_matrix(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        selected_row = choose_row(matrix)
        sign = (-1) ** selected_row
        total = 0
        for col_j, entry in enumerate(matrix[selected_row]):
            if entry != 0:
                minor = i_j_minor(matrix, selected_row, col_j)
                total += sign * entry * determinant_of_matrix(minor)
            sign *= -1
        return total


if __name__ == '__main__':
    matrix_a = [[1, 0, 2, -1],
                [3, 0, 0, 5],
                [2, 1, 4, -3],
                [1, 0, 5, 0]]

    print(i_j_minor(matrix_a, 1, 1))
    print(choose_row(matrix_a))
    print(determinant_of_matrix(matrix_a))

    matrix_b = np.array(matrix_a)
    print("the determinant of the given matrix is", np.linalg.det(matrix_b))