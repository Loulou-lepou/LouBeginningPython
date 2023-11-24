"""
 1. validate 2 input matrices A_(m x n) and B_(n x p)
 2. check if # columns of A = # rows of B
 3. If matrix multiplication b/w A & B is valid,
 return the product matrix C_(m x p)
 else return an error message "The matrices A & B cannot be multiplied."
"""
import numpy as np


def input_matrix(num_rows, num_cols):
    """
    Validate an input matrix with the given numbers of rows and columns.
    """
    matrix = []
    for _ in range(num_rows):
        while True:
            row = input(f"Enter {num_cols} elements separated by a comma: ")\
                .strip().split(',')
            if len(row) == num_cols:
                try:
                    matrix.append([int(element) for element in row])
                    break
                except ValueError:
                    print("Invalid inputs. Please enter integers only.")
            else:
                print(f"Invalid number of elements. Expected {num_cols} elements.")

    return matrix


def multiply_matrices(matrix_a, matrix_b):
    """
    Multiply two matrices and return the product matrix if valid dimensions,
    otherwise return None.
    """
    num_rows_a = len(matrix_a)
    num_cols_a = len(matrix_a[0])
    num_rows_b = len(matrix_b)
    num_cols_b = len(matrix_b[0])

    if num_cols_a != num_rows_b:
        return None
    else:
        product_matrix = [[0 for _ in range(num_cols_b)] for _ in range(num_rows_a)]

        for i in range(num_rows_a):
            for j in range(num_cols_b):
                for k in range(num_cols_a):
                    product_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return np.array(product_matrix)


if __name__ == '__main__':
    # Enter dimensions of matrices
    rows_a = int(input("Enter the number of rows for matrix A: "))
    cols_a = int(input("Enter the number of columns for matrix A: "))
    rows_b = int(input("Enter the number of rows for matrix B: "))
    cols_b = int(input("Enter the number of columns for matrix B: "))

    # Input matrices
    print("Enter elements for matrix A:")
    mat_a = input_matrix(rows_a, cols_a)
    print()

    print("Enter elements for matrix B:")
    mat_b = input_matrix(rows_b, cols_b)
    print()

    print("Matrix A:\n", mat_a)
    print("Matrix B:\n", mat_b)

    # Multiply matrices
    product_mat = multiply_matrices(mat_a, mat_b)
    if product_mat is not None:
        print("The product matrix is:\n", product_mat)
    else:
        print("The matrices A & B cannot be multiplied.")
