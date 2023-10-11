# https://practice.geeksforgeeks.org/problems/multiply-matrices/
# multiply 2 given square matrices
# Problem solved successfully 100/100, 0.07 sec

def multiply(matrix_a, matrix_b):
    size = len(matrix_a)
    matrix_c = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            entry_c = 0
            for k in range(size):
                entry_c += matrix_a[i][k] * matrix_b[k][j]
            matrix_c[i][j] = entry_c
    return matrix_c


def read_matrix(num_rows):
    arr = list(map(int, input("Enter the matrix elements in a row-wise array:\n").strip().split()))
    input_mat = [[0 for _ in range(num_rows)] for _ in range(num_rows)]
    c = 0
    for row_index in range(num_rows):
        for col_index in range(num_rows):
            input_mat[row_index][col_index] = arr[c]
            c += 1
    return input_mat


if __name__ == '__main__':
    num_test_cases = int(input("Enter the number of test cases: "))
    for _ in range(num_test_cases):
        n = int(input())
        matrix_1 = read_matrix(n)
        matrix_2 = read_matrix(n)

        matrix_3 = multiply(matrix_1, matrix_2)
        for row_i in range(n):
            for col_j in range(n):
                print(matrix_3[row_i][col_j], end=" ")
        print('')
