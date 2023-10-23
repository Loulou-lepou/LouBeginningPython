import math as m


def sieve_of_eratosthenes(num):
    # num > 1
    if num == 3:
        return [2]
    elif num == 2:
        return []
    else:
        # indices of bool_array : from 0 to num - 1
        bool_index = [True for _ in range(0, num + 1)]
        for i in range(3, int(m.sqrt(num)) + 1, 2):
            if bool_index[i]:
                for multiple_id in range(i * i, num + 1, 2 * i):
                    bool_index[multiple_id] = False

        primes = [i for i in range(3, num, 2) if bool_index[i]]
        primes.insert(0, 2)
        return primes


def sum_divisors(num):
    if num == 1:
        return 1
    else:
        upper_bound = m.sqrt(num)
        total = 0
        for i in range(1, m.floor(upper_bound) + 1):
            if num % i == 0:
                total += i + num // i
        if upper_bound.is_integer():
            total -= int(upper_bound)

        return total


def is_prime(num):
    if num == 1:
        return False
    else:
        for _ in range(2, int(m.sqrt(num)) + 1):
            if num % _ == 0:
                return False
        return True


def prime_factors(num):
    # prime_upto_num = sieve_of_eratosthenes(num + 1)
    primes, powers = [], []
    for p in sieve_of_eratosthenes(int(m.sqrt(num)) + 2):
        # print("num = ", num, "p = ", p)
        if num % p == 0:
            primes.append(p)
            power = 0
            while num % p == 0:
                power += 1
                num //= p
            powers.append(power)
        if num == 1:
            break
        if num > 1 and is_prime(num):
            primes.append(num)
            powers.append(1)
            break
    return primes, powers


def gp_sum(prime_factor_k, alpha_k):
    return (prime_factor_k ** (alpha_k + 1) - 1) // (prime_factor_k - 1)


def sum_factors(num):
    prime_divisors, exponents = prime_factors(num)

    prod_ = 1
    for p_k, power_k in zip(prime_divisors, exponents):
        prod_ *= gp_sum(p_k, power_k)
    # for i in range(len(prime_divisors)):
    #    prod_ *= gp_sum(prime_divisors[i], exponents[i])
    return prod_


class Solution:
    def sumOfDivisors(self, n):
        # -------------- failed 1012/ 1115 --------------------
        # sum_ = 0
        # for j in range(1, N + 1):
        #     sum_ += sum_divisors(j)
        # return sum_

        # ---------use sieve of eratosthenes -------------------
        # --------- failed 1012/1115 ---------------------------
        # prime_numbers = set(sieve_of_eratosthenes(n + 1))
        # composite_numbers = set(range(2, n + 1)) - prime_numbers
        # sum_ = 0
        # for prime in prime_numbers:
        #     sum_ += (1 + prime)
        # for composite in composite_numbers:
        #     # sum_ += sum_factors(composite)
        #     sum_ += sum_divisors(composite)
        # return sum_ + 1

        # ------------------ best approach -----------------------
        # ------------ problem solved successfully 1115/1115 -----
        if n == 0:
            return 0
        else:
            # each number i,  1 <= i <= n appears in the sum (n // i) times
            return sum([i * (n // i) for i in range(1, n + 1)])


if __name__ == '__main__':
    num_testcases = int(input('Number of testcases = '))
    for _ in range(num_testcases):
        n_ = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(n_)
        print(ans)
