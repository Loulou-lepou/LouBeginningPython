# Euclidean algorithm to compute gcd(a, b)
# Expressing gcd as a linear combination of a and b
# https://en.wikipedia.org/wiki/Euclidean_algorithm
def gcd(a, b):
    # a < b => swap a & b
    a, b = max(a, b), min(a, b)

    q, r = a // b, a % b
    print(f'{a} =  {b} * {q} + {r}')

    # Bezout's coefficients s, t
    # b | a => gcd = b = 0 * a + 1 * b
    s_old, t_old = 0, 1

    if r > 0:
        quotients, remainders = [], []
        while r > 0:
            quotients.append(q)
            remainders.append(r)
            a, b = b, r
            q, r = a // b, a % b
            print(f'{a} = {b} * {q} + {r}')

        # a = b * q0 + r0, b = r0 * q1 + r1
        # r_(i) = q_(i + 1) * r_(i + 1) + r_(i + 2)
        # q = [q0, q1, q2, ..., q_k], r = [r0, r1, r2, ..., r_k]
        # print('q = ', quotients)
        # print('r = ', remainders)

        num_steps = len(remainders)
        print(f'# steps = {num_steps}')

        # gcd(a, b) = last non-zero remainder r_k = remainders[# steps - 1]
        # out of while loop, r_k = b, r_(k + 1) = 0

        # Compute Bezout's coefficients s, t: gcd(a, b) = a * s + b * t
        s_old, t_old = 1, - quotients[- 1]
        for i in range(num_steps - 2, -1, -1):
            s_new = t_old
            t_new = -t_old * quotients[i] + s_old
            # print(f'q[{i}] = {quotients[i]}, s = {s_new}, t = {t_new}')
            s_old, t_old = s_new, t_new

    return b, s_old, t_old


if __name__ == '__main__':
    print('Enter 2 numbers separated by a space')
    # 2250, 154  / 1071, 462
    a1, b1 = map(int, input('').split(' '))
    d, s, t = gcd(a1, b1)
    print(f'gcd is a linear combination: gcd({a1}, {b1}) = {d} = {s} * {max(a1, b1)} + {t} *{min(b1, a1)}')
