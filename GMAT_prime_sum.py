"""
The Official Guide for GMAT, Quantitative Review 2017. E73, p71
The prime sum of an integer n greater than 1 is the sum of all the prime factors of n, including repetitions.
For example, the prime sum of 12 is 7, since 12 = 2 x 2 x 3 and 2 + 2 + 3 = 7.
For which of the following integers is the prime sum greater than 35?
440, 512, 620, 700, 750

"""

import math as m


def sieve_of_eratosthenes(num):
    # all prime numbers up to (<) 'num'
    # bool_list -> mark whether a number is prime or not
    bool_list = [True] * (num + 1)
    if num <= 2:
        return [2]
    else:
        upper_bound = m.floor(m.sqrt(num)) + 1
        for p in range(3, upper_bound, 2):
            if bool_list[p]:
                for i in range(p ** 2, num + 1, 2 * p):
                    bool_list[i] = False
        primes = [_ for _ in range(3, num, 2) if bool_list[_]]
        primes.insert(0, 2)
        return primes


def prime_factorization(num):
    prime_list = sieve_of_eratosthenes(m.floor(m.sqrt(num)) + 1)
    prime_factors = []
    powers = []
    for prime in prime_list:
        if num % prime == 0:
            count = 0
            prime_factors.append(prime)
            while num % prime == 0:
                num //= prime
                count += 1
            powers.append(count)
            if num == 1:
                break
    if num > 1:
        prime_factors.append(num)
        powers.append(1)
    return prime_factors, powers


def prime_sum(num):
    prime_divisors, exponents = prime_factorization(num)
    sum_ = 0
    for _ in range(len(prime_divisors)):
        sum_ += prime_divisors[_] * exponents[_]
    return sum_


if __name__ == '__main__':
    user_input = map(int, input("Enter a list of numbers, separated by a comma").strip().split(","))
    correct = [number for number in user_input if prime_sum(number) >= 35]
    print(correct)
    print([prime_factorization(_) for _ in correct])
