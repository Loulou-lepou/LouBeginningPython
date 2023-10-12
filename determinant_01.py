import numpy as np


def i_j_minor(matrix, n, i, j):
    # list is mutable
    # some_list.remove()  -> NoneType object
    row_list = list(range(n))
    row_list.remove(i)
    col_list = list(range(n))
    col_list.remove(j)
    mat = [[0 for _ in range(n - 1)] for _ in range(n - 1)]
    r = 0
    for row_index in row_list:
        c = 0
        for col_index in col_list:
            mat[r][c] = matrix[row_index][col_index]
            c += 1
        r += 1
    return mat


def choose_row(matrix, n):
    best_row = 0
    min_nonzeroes = n
    for row_id in range(n):
        count_nonzeroes = np.count_nonzero(matrix[row_id])
        if count_nonzeroes < min_nonzeroes:
            min_nonzeroes = count_nonzeroes
            best_row = row_id
    return best_row


def determinant_of_matrix(matrix, n):
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        # choose the row with many zeroes
        selected_row = choose_row(matrix, n)
        print(selected_row)
        print(matrix[selected_row])
        # apply Laplace expansion along a row
        sign = (-1) ** selected_row
        total = 0
        for col_j in range(n):
            next_entry = matrix[selected_row][col_j]
            if next_entry != 0:
                minor = i_j_minor(matrix, n, selected_row, col_j)
                total += sign * next_entry * determinant_of_matrix(minor, n - 1)
                print(f"{sign} * {matrix[selected_row][col_j]} "
                      f"* det ({i_j_minor(matrix, n, selected_row, col_j)})"
                      f"= {sign * next_entry * determinant_of_matrix(minor, n - 1)}")
            sign *= -1
        return total


if __name__ == '__main__':
    matrix_a = [[1, 0, 2, -1],
                [3, 0, 0, 5],
                [2, 1, 4, -3],
                [1, 0, 5, 0]]
    size = len(matrix_a)
    num_i, num_j = 1, 1
    print(i_j_minor(matrix_a, size, num_i, num_j))
    print(choose_row(matrix_a, size))
    print(matrix_a[choose_row(matrix_a, size)])
    print(determinant_of_matrix(matrix_a, size))
    # compare with result ran by np.linalg.det()
    matrix_b = np.array(matrix_a)
    print("using np.linalg.det, the determinant of the given matrix is ", np.linalg.det(matrix_b))
