# compute determinant, inverse matrix using np.linalg.det / np.linalg.inv
# compute inverse matrix using adj matrix
import numpy as np


def get_cofactor(arr, i, j):
    # use np.delete(arr, i, axis = 0) to delete row i
    # use np.delete(arr, j, axis = 1) to delete col j
    c = np.delete(np.delete(arr, i, axis=0), j, axis=1)
    return (-1)**(i + j) * np.linalg.det(c)


if __name__ == '__main__':

    n_array = np.array([[1, 2, 3],
                        [0, 1, 4],
                        [5, 6, 0]])
    print("the given matrix is \n", n_array)
    det1 = np.linalg.det(n_array)
    print("its determinant is", np.linalg.det(n_array))

    if det1 != 0:
        # step 1 : transpose the original matrix
        b = n_array.transpose()
        print("its transpose is \n", b)
        # step 2 : get the adj matrix
        a = np.zeros((3, 3))
        for i1 in range(3):
            for j1 in range(3):
                a[i1, j1] = get_cofactor(b, i1, j1)
        print("the adj matrix is \n", a)
        print("Using adj matrix, the inverse matrix is \n", a / det1)
        print("its inverse is \n", np.linalg.inv(n_array))
