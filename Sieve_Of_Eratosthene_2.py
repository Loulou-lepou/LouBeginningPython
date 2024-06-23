# Given n, list all primes <= n
# Ref links:
# 1. https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# 2. https://www.javainterviewpoint.com/python-sieve-of-eratosthenes/
# 3. https://www.geeksforgeeks.org/sieve-of-eratosthenes/
# 4. https://www.invivoo.com/en/the-sieve-of-eratosthenes/
# Pseudocode:
# algorithm Sieve of Eratosthenes
# input: an integer n > 1
# Output: all prime numbers from 2 through n
# let A be an array of Boolean values, indexed by integers 2 to n
# initially all set to be true
# for i = 2.. floor(sqrt(n)) do
# if A[i] is true
#      for j = i^2.. n do
#            A[j] := false
# return all i such that A[i] is true
# Time complexity: O(n*(log(log n)))
# given array update is O(1) operation

# --------------------------------------------------------------
#                  naive solution 1 (Lou lou)
#
#             need some refinements R(1), R(2), R(3), R(4)
# --------------------------------------------------------------
import math as m
import timeit


def sieve_of_eratosthenes_1(n):
    a = [1 for _ in range(2, n + 1)]
    l1 = []
    # R(1): math module to compute sqrt(n), int function to calculate floor(sqrt(n))
    for _ in range(2, int(m.sqrt(n)) + 1):
        if a[_ - 2] == 1:
            # R(2): compare the entry with 1
            # R(3): compute _ - 2 to match the number in list a
            for j in range(_ ** 2, n + 1, _):
                a[j - 2] = 0
    # R(4): one more for loop & if cond to print primes <= n
    for _ in range(2, n + 1):
        if a[_ - 2] == 1:
            l1.append(_)
    return l1

# --------------------------------------------------------------
#                     solution 2
#
# --------------------------------------------------------------


def sieve_of_eratosthenes_2(n):
    # refinement R(2): create a boolean array
    prime_list = [True for _ in range(n + 1)]
    # Initialize p = 2 the smallest prime number
    p = 2
    # refinement R(1): without using math module, floor function
    while p * p <= n:
        # refinement R(3): without having to compare entries with 1
        # If prime[p] is not changed, then it is a prime
        # refinement : prime_list[p] == True ->  Expression can be simplified
        # PEP8:E712 comparison to True should be 'if cond is True:' or 'if cond:'
        if prime_list[p]:
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime_list[i] = False
        # increase p by 1
        p += 1

    # Print all prime numbers R(4)
    for p in range(2, n + 1):
        if prime_list[p]:
            print(p, end=' ')

# --------------------------------------------------------------
#                     solution 3
#
# --------------------------------------------------------------


def sieve_of_eratosthenes_3(n):
    # 1. Create a list of consecutive integers from 2 through n
    my_list = list(range(2, n + 1))
    # 2. Initially, let p = 2, the smallest prime number
    for i in range(2, int(m.sqrt(n) + 1)):
        # 3. Enumerate the multiples of p by counting in increments of
        #    i from i^2 to n (i^2 < n) and mark them in the list
        #    where i itself should not be marked
        for j in range(i * i, n + 1, i):
            if j in my_list:
                my_list.remove(j)
    return my_list


# --------------------------------------------------------------
#                     solution 4
#
# --------------------------------------------------------------
# Initially list odd numbers only (3, 5,...,n)
# count in increments of 2p from p^2 (marking only odd multiples of p)
def sieve_of_eratosthenes_4(n):
    a = [True for _ in range(1, n + 1)]
    for i in range(3, int(m.sqrt(n)) + 1, 2):
        if a[i]:
            for j in range(i * i, n + 1, 2 * i):
                a[j] = False
    prime_list = [2]
    for i in range(3, n + 1, 2):
        if a[i]:
            prime_list.append(i)
    return prime_list


# -------last reviewed 22 Jun 2024 ----------
# define meaningful names for variables

def sieve_of_eratosthenes_5(n):
    prime_check = [True for _ in range(1, n + 1)]
    for i in range(3, int(m.sqrt(n)) + 1, 2):
        if prime_check:
            for j in range(i * i, n + 1, 2 * i):
                prime_check[j] = False

    primes = [2] + [i for i in range(3, n + 1, 2) if prime_check[i]]
    return primes
    

if __name__ == '__main__':
    n1 = int(input('n = '))
    print(f'Prime numbers up to {n1}:')

    start = timeit.default_timer()
    print(*sieve_of_eratosthenes_1(n1))
    stop = timeit.default_timer()
    t1 = stop - start
    print('Time for running Algorithm 1 = ', stop - start)

    # print(*sieve_of_eratosthenes_3(n1))

    # sieve_of_eratosthenes_2(n1)

    start = timeit.default_timer()
    print(*sieve_of_eratosthenes_4(n1))
    stop = timeit.default_timer()
    t2 = stop - start
    print('Time for running Algorithm 4 = ', stop - start)
