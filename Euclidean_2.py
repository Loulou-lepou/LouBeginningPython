# Euclidean algorithm to compute gcd(a, b)
# Expressing gcd as a linear combination of a and b
# https://en.wikipedia.org/wiki/Euclidean_algorithm
def gcd(a, b):
    # if a < b, swap the numbers
    a, b = max(a, b), min(a, b)
    r = a % b
    # Bezout's coefficients
    s_old, t_old = 0, 1
    # k = # steps in Euclidean algorithm
    k = 0
    # remainders decrease with every step but can never be negative
    # remainder r_k must eventually = 0
    print(f'{a} {b} {r}')
    if r > 0:
        quotient_list = []
        remainder_list = []
        while r > 0:
            quotient_list.append(a // b)
            remainder_list.append(r)
            a = b
            b = r
            r = a % b
            k += 1
            print(f'{a} {b} {r}')

        # q = [q0, q1, q2, ..., q_(k)]
        # r = [r0, r1, r2, ..., r_(k)]
        # a = b * q0 + r0, b = r0 * q1 + r1
        # recursive formula r_(i) = q_(i + 1) * r_(i + 1) + r_(i + 2)
        print('q = ', quotient_list)
        print('r = ', remainder_list)
        # the last non-zero remainder r_k = remainder_list[k - 1] is gcd(a, b)
        # out of while loop, r_k = b

        # Compute s, t: gcd(a, b) = a * s + b * t
        # len(q) = len(r) = k + 1
        s_old = 1
        t_old = - quotient_list[k - 1]
        print('s = ', s_old, 't = ', t_old)

        for i in range(k - 1, 0, -1):
            s_new = t_old
            t_new = -t_old * quotient_list[i - 1] + s_old
            print('i = ', i, ', q[i] = ', quotient_list[i - 1], ', s = ', s_new, ', t = ', t_new)
            s_old = s_new
            t_old = t_new
    # # steps = k is finite since # non-negative integers in [0, b) is finite
    print(f'# steps = {k}')
    return b, s_old, t_old


if __name__ == '__main__':
    print('Enter 2 numbers separated by a space')
    # 2250, 154  / 1071, 462
    a1, b1 = map(int, input('').split(' '))
    d, s, t = gcd(a1, b1)
    print(f'gcd is a linear combination: gcd({a1}, {b1}) = {d} = {s} * {a1} + {t} *{b1}')
