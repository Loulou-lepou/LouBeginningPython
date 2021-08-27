# Given a number, count all distinct divisors of it.
# O(sqrt(n)) -> naive solution
# Ref : https://www.themathdoctors.org/counting-divisors-of-a-number/
import math


# function to count the divisors
def count_divisors(n):
    cnt = 0
    for _ in range(1, int(math.sqrt(n)) + 1):
        if n % _ == 0:
            # If divisors are equal,
            # count only one
            if n / _ == _:
                cnt = cnt + 1
            else:  # Otherwise count both
                cnt = cnt + 2

    return cnt


# Driver program
if __name__ == '__main__':
    print("Total distinct divisors of 1000 are : ",
          count_divisors(1000))
    # Find the number less than 100 that has the greatest number of factors
    max_cnt = 2
    l_1 = []
    l_cnt = []
    l_max = []
    for _ in range(6, 100):
        k = count_divisors(_)
        if k >= max_cnt:
            max_cnt = count_divisors(_)
            l_1.append(_)
            l_cnt.append(k)
    for _ in range(1, len(l_cnt)):
        if l_cnt[_] == max_cnt:
            l_max.append(l_1[_])

    print(f'The numbers < 100 that have the greatest number of factors = {max_cnt}')
    print(l_max)
