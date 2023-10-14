# https://practice.geeksforgeeks.org/contest/gfg-weekly-coding-contest-123/problems
# Find Bots on Geeklandster:  Problem solved successfully
"""
There are a lot of bots on one of the popular social media platform "GeeklandSter".
Now since GeeklandSter has been acquired by the richest man of Geekland, he wants to
remove every bot from his platform. Geek used his magical powers and determined that
the count of distinct characters at even positions (0th, 2nd, 4th,...) of username
is a prime number for every bot.
U have been given an array of strings usernames[], and for each of them tell if the user
is a bot or not by returning an array of integers where 0 corresponds to the human and 1
corresponds to the bot.
Example 1:
Input:
n = 4
usernames = {"abcdef", "pqrs", "xyzuvabb", "aaaaaa"}
Output:
answer = {1, 1, 0, 0}
"""
from typing import List
import math as m


def is_prime(num):
    if num == 1:
        return 0
    elif num in {2, 3}:
        return 1
    else:
        for i in range(2, m.floor(m.sqrt(num)) + 1):
            if num % i == 0:
                return 0
        return 1


class Solution:
    def findBots(self, usernames: List[str], n: int) -> List[int]:
        answer = []
        for name in usernames:
            even_char = set(name[::2])
            # print(name[::2])
            # print(even_char)
            # print(len(even_char))
            # print(is_prime(len(even_char)))
            answer.append(is_prime(len(even_char)))
        return answer


class StringArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = input().strip().split()  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        usernames = StringArray().Input(n)
        obj = Solution()
        res = obj.findBots(usernames, n)
        IntArray().Print(res)
