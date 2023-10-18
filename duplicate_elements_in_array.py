class Solution:
    def duplicates(self, arr):
        seen = set()
        duplicates = set()
        for element in arr:
            if element not in seen:
                seen.add(element)
            else:
                duplicates.add(element)
        return sorted(duplicates) if duplicates != set() else [-1]


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        input_arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(input_arr)
        for _ in res:
            print(_, end=" ")
        print()
