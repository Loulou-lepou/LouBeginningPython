# Given a matrix of size n x m,
# where every row and column is sorted in increasing order, and a number x.
# Find whether element x is present in the matrix or not.
# https://practice.geeksforgeeks.org/problems/search-in-a-matrix-1587115621/
# https://practice.geeksforgeeks.org/problems/search-in-a-matrix17201720/0
# Problem solved successfully 86/86, 0.69 sec (the best method); 247/247, 0.89 sec

class Solution:

    def search_element(self, matrix, num_rows, num_columns, target_number):
        if target_number < matrix[0][0] \
                or target_number > matrix[num_rows - 1][num_columns - 1]:
            return 0
        else:
            row = 0    # start from the first row
            col = num_columns - 1       # start from the final column
            while row < num_rows and col >= 0:
                if matrix[row][col] == target_number:
                    return 1            # found the target_number
                elif matrix[row][col] > target_number:
                    # remaining elements in column col > target_number
                    # skip column col, move to the next left column
                    col -= 1
                else:
                    # matrix[row][col] < target_number
                    # remaining elements in the current row < target_number
                    # skip the current row, move on to the next downwards row
                    row += 1
        return 0


if __name__ == '__main__':
    num_testcases = int(input())
    for _ in range(num_testcases):
        # enter number of rows and number of columns
        size = input().strip().split()
        num_row = int(size[0])
        num_col = int(size[1])
        # enter matrix elements in a row-wised array
        # .strip() method to remove leading and trailing whitespaces
        # .split() method to separate numbers with a default delimiter (a whitespace)
        line = input().strip().split()
        # initialize a zero matrix_a with the given dimension
        matrix_a = [[0 for _ in range(num_col)] for _ in range(num_row)]
        # read the matrix from the row-wised array
        for i in range(num_row):
            for j in range(num_col):
                matrix_a[i][j] = int(line[i * num_col + j])
        # enter the target number x
        target = int(input())
        obj = Solution()
        if obj.search_element(matrix_a, num_row, num_col, target):
            print(1)
        else:
            print(0)
