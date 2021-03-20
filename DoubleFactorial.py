# n!! = 1 x 3 x 5 x... x n  if n is odd
# n!! = 2 x 4 x 6 x ... x n  if n is even
# compute n !! %  100000007 for a given integer input n


def prod_odd(k):
    p = 1
    for _ in range(1, k + 1, 2):
        p = p * _
        if p >= 100000007:
            p = p % 100000007
    return p


def prod_2(k2):
    p2 = 1
    for _ in range(1, k2 + 1):
        p2 = p2 * _
        if p2 >= 100000007:
            p2 = p2 % 100000007
    return p2


if __name__ == '__main__':
    n = int(input())
    if 0 < n < 10 ** 7:
        if n % 2 == 1:
            print(prod_odd(n))
        else:
            d = n // 2
            d1 = (2 ** d) % 100000007
            print((d1 * prod_2(d)) % 100000007)
