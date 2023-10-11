# https://practice.geeksforgeeks.org/problems/kth-element-in-matrix
# given a N x N matrix, where every row and column is sorted in non-decreasing order.
# Fidn the kth smallest element in the matrix.
# Problem solved successfully 105/105, 0.18 sec

def kthSmallest(mat, n, k):
    arr = [0 for _ in range(n * n)]
    for i in range(n):
        for j in range(n):
            # before mat[i][j]:  i previous rows: row 0 -> row (i - 1)
            # j previous entries in row i: mat[i][0] -> mat[i][j - 1]
            arr[i * n + j] = mat[i][j]
    arr.sort()
    # print(arr)
    return arr[k - 1]


if __name__ == "__main__":

    T = int(input())
    while T > 0:
        len_mat = int(input())
        matrix_mat = [[0 for j in range(len_mat)] for i in range(len_mat)]
        line1 = [int(x) for x in input().strip().split()]
        num_k = int(input())

        temp = 0
        for i in range(len_mat):
            for j in range(len_mat):
                matrix_mat[i][j] = line1[temp]
                temp += 1

        print(kthSmallest(matrix_mat, len_mat, num_k))
        T -= 1
