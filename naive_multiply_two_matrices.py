"""
 1. validate 2 input matrices A_(m x n) and B_(n x p)
 2. check if # columns of A = # rows of B
 3. If matrix multiplication b/w A & B is valid,
 return the product matrix C_(m x p)
 else return an error message "The matrices A & B cannot be multiplied."
"""
import numpy as np


def input_integer(prompt_message):
    """ validate an input real number """
    while True:
        try:
            return int(input(prompt_message))
        except ValueError:
            print("Invalid input")


def input_list_2(given_length):
    """ validate the user's list """

    while True:
        add_s = "s separated by a comma" if given_length > 1 else ""
        list_str = input("Enter " + str(given_length) + " element" + add_s)\
            .strip().split(',')

        if len(list_str) == given_length:
            try:
                return [float(element) for element in list_str]
            except ValueError:
                print("Invalid inputs")
        else:
            print("Invalid inputs")


def input_matrix(num_rows, num_cols):
    """
    validate an input matrix with the given numbers of rows and columns
    using list comprehension and nested list
    """
    mat = []
    count = 0
    while count < num_rows:
        new_row = input_list_2(num_cols)
        if new_row is not None:
            mat.append(new_row)
            count += 1

    return np.array(mat)


def input_matrix_2():
    """
    generate 2 matrices of integers using np.random.randint(start, stop, size)
    """
    np.random.seed(27)
    matrix_1 = np.random.randint(1, 10, size=(3, 3))
    matrix_2 = np.random.randint(1, 10, size=(3, 3))
    return matrix_1, matrix_2


def multiply_matrices(mat_1, mat_2):
    """ return the product matrix """
    # check if matrix multiplication is valid
    mat1_num_cols = len(mat_1[0])
    mat1_num_rows = len(mat_1)
    mat2_num_rows = len(mat_2)
    mat2_num_cols = len(mat_2[0])

    product_matrix = [[0 for _ in range(mat2_num_cols)]
                      for _ in range(mat1_num_rows)]

    if mat1_num_cols == mat2_num_rows:

        for row_i in range(mat1_num_rows):
            mat1_row_i = np.array(mat_1[row_i])
            for col_j in range(mat2_num_cols):
                mat2_col_j = np.array([mat_2[_][col_j]
                                       for _ in range(mat2_num_rows)])
                product_matrix[row_i][col_j] = sum(mat1_row_i * mat2_col_j)

        return np.array(product_matrix)


if __name__ == '__main__':

    # Enter dimensions of matrices

    rows_a = input_integer("Enter the number of rows for matrix A: ")
    cols_a = input_integer("Enter the number of columns for matrix A: ")
    rows_b = input_integer("Enter the number of rows for matrix B: ")
    cols_b = input_integer("Enter the number of columns for matrix B: ")

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

    # multiply matrices using np.dot()
    print(f"Using np.dot(mat_a, mat_b), the product matrix is:\n",
          np.dot(mat_a, mat_b))

    # multiply matrices using np.matmul()
    print(f"Using np.matmul(mat_a, mat_b), the product matrix is:\n",
          np.matmul(mat_a, mat_b))

    # multiply matrices using '@'
    print(f"Using @, the product matrix is:\n",
          mat_a @ mat_b)
