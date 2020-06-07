from numpy import array


def gauss_partial_pivoting(a):

    m = a.shape[0]
    n = a.shape[1]

    for k in range(m):

        # linear search -> find max_element in col k, below a[k][k]
        max_element = abs(a[k][k])
        max_row = k
        for i in range(k+1, m):
            if abs(a[i][k]) > max_element:
                max_element = abs(a[i][k])
                max_row = i

        # swap Row k and Row max_row
        if max_row != k:
            for j in range(k, n):
                tmp = a[max_row][j]
                a[max_row][j] = a[k][j]
                a[k][j] = tmp

        # For all rows i below pivot a[k][k] != 0
        if a[k][k] != 0:
            for i in range(k+1, m):
                c = - a[i][k]/a[k][k]
                for j in range(k+1, n):
                    a[i][j] = a[i][j] + c * a[k][j]
                # fill lower triangular matrix with zeros
                a[i][k] = 0
    return a


if __name__ == '__main__':
    # user enters the matrix or import the matrix

    matrix_a = array([[1, 3, 1, 3],
                      [2, 0, 7, 0],
                      [1, 0, -2, 17]], float)
    print("matrix A = \n", matrix_a)

    print("Performing Gaussian Elimination with partial pivoting,"
          "\nwe get the row echelon form of A = \n",
          gauss_partial_pivoting(matrix_a))
