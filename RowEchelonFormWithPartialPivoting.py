from numpy import array


def gauss_partial_pivoting(a):

    n = a.shape[0]
    m = a.shape[1]

    for k in range(n):

        # linear search ->find max_element in col k, below a[k][k]
        max_element = abs(a[k][k])
        max_row = k

        for i in range(k+1, n):
            if abs(a[i][k]) > max_element:
                max_element = abs(a[i][k])
                max_row = i

        if max_row != k:
            # switch Row k and Row max_row
            for j in range(k, m):
                tmp = a[max_row][j]
                a[max_row][j] = a[k][j]
                a[k][j] = tmp

        # eliminate all rows below a[k][k]
            for i in range(k+1, n):
                c = - a[i][k]/a[k][k]
                for j in range(k+1, m):
                    a[i][j] = a[i][j] + c * a[k][j]
                a[i][k] = 0
    return a


if __name__ == '__main__':
    # user enters the matrix or import the matrix

    matrix_a = array([[1, 1, 1, 3],
                      [2, 3, 7, 0],
                      [1, 3, -2, 17]], float)
    print("matrix A = \n", matrix_a)

    print("Performing Gaussian Elimination with partial pivoting,"
          "\nwe get the row echelon form of A = \n",
          gauss_partial_pivoting(matrix_a))
