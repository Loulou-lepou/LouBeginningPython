# Euclidean algorithm to compute gcd(a, b)
# Expressing gcd as a linear combination of a and b
# https://en.wikipedia.org/wiki/Euclidean_algorithm
def gcd(a, b):
    # if a < b, swap the numbers
    a, b = max(a, b), min(a, b)
    r = a % b
    k = 1
    # remainders decrease with every step but can never be negative
    # remainder r_k must eventually = 0
    print(f'{a} {b} {r}')
    if r > 0:
        while r > 0:
            a = b
            b = r
            r = a % b
            k += 1
            print(f'{a} {b} {r}')
        # # steps = k is finite since # non-negative integers in [0, b) is finite
        print(f'# steps = {k}')
    # the last non-zero remainder r_k is gcd(a, b)
    return b


if __name__ == '__main__':
    print('Enter 2 numbers separated by a space')
    # 2250, 154  / 1071, 462
    a1, b1 = map(int, input('').split(' '))
    print(f'gcd({a1}, {b1}) = {gcd(a1, b1)}')
