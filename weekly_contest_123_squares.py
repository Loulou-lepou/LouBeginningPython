# https://practice.geeksforgeeks.org/contest/gfg-weekly-coding-contest-123/problems
# Squares:  Problem solved successfully
# Initially given a square of side = 2 ^ N, u can perform following operation:
# Pick any square, if the side of the square is 2 ^ M (M > 0)
# then you can divide this square into four smaller squares of side = 2 ^ (M - 1)
# and replace the bigger square with these 4 squares.

# U can perform as many operations as u want.
# Ur task is to find minimum number of operations needed to make at least X boxes.
# If it is not possible to make X boxes return -1.
import math as m


def max_operations(num):
    # s_n = 1 + 4 * s_(n - 1), s_1 = 1
    # s_n = max_operations that can be performed on the square of side 2 ^ N
    # u_n = s_n + 1 / 3 = 4 * (s_(n - 1) + 1 / 3) = 4 * u_(n - 1)
    # u_1 = s_1 + 1 / 3 = 4 / 3
    # u_n = (4 / 3) * 4 ^ (n - 1) => s_n = (4 / 3) *  4 ^ (n - 1) - 1 / 3
    return round((4 / 3) * 4 ** (num - 1) - 1 / 3)

    # if num == 1:
    #     return 1
    # else:
    #     total = 1
    #     for i in range(2, num + 1):
    #         total = 1 + 4 * total
    #     return total


def max_boxes(num_operations):
    # initially, there's only 1 box
    # each operation increases the number of boxes by 3
    return 1 + num_operations * 3


class Solution:
    def squares(self, N, X):
        # substitute the explicit algebraic formula for s_n, then max_boxes = 4 ** N
        # max_boxes(max_operations(N)) = 4 ^ n
        if X > 4 ** N:
        # if X > max_boxes(max_operations(N)):
            return -1
        else:
            # the max_boxes after performing (num_operations - 1) operations < X
            # the max_boxes after performing num_operations >= X
            return m.ceil((X - 1) / 3)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, X = map(int, input().strip().split())
        ob = Solution()
        ans = ob.squares(N, X)
        print(ans)
