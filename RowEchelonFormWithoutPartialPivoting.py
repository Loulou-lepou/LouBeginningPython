#! /usr/bin/env python3
# Ref : Gaussian Elimination Method Tutorial
# - Part 1 : Basic procedure (Numerical Methods with Python)
# Author :


from numpy import array, zeros


a = array([[3, -2, 5, 0],
          [4, 5, 8, 1],
          [1, 1, 2, 1],
          [2, 7, 6, 5]], float)
print("Matrix A = \n", a)
n = len(a.shape[1])

# Row echelon form without partial pivoting
for k in range(n):
    if a[k, k] != 0:
        for i in range(k+1, n):
            for j in range(k+1, n):
                a[i, j] = a[i, j] - a[k, j] * a[i, k] / a[k, k]
            a[i, k] = 0
print("Row Echelon Form of A = \n", a)
