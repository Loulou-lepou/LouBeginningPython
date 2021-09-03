# Divisibility rules

# divisibility rule for 2.
# n is divisible by 2 if its last digit is in [0, 2, 4, 6, 8]
def divisible_by_two(n: str) -> bool:
    last_digit = n[-1]
    return last_digit in ['0', '2', '4', '6', '8']


# divisibility rule for 3
# n is divisible by 3 if the sum of its digits is divisible by 3.
def divisible_by_three(n: str) -> bool:
    total_digit = 0
    for str_digit in n:
        total_digit = (total_digit + int(str_digit)) % 3
    return total_digit == 0


# divisibility rule for 7 [Medium level]
# https://www.geeksforgeeks.org/check-whether-large-number-divisible-7/
# n % 7 = (alternating sum of blocks of 3 from right to left) % 7
# for each block of 3 : abc = 2 * a + 3 * b + c (mod 7)
def divisible_by_seven(n: str) -> bool:
    k = len(n)
    if (k % 3) != 0:
        # if k % 3 == 1, append two 0s at the beginning
        # if k % 3 == 2, append one 0s at the beginning
        n = '0' * (3 - (k % 3)) + n
        k = k + 3 - (k % 3)
    # n_blocks = # blocks of 3 form right to left
    n_blocks = k // 3
    alt_sum = 0
    # pos_3 = position of the last digit in the block of 3 (from right to left)
    # initialize pos_3 = the last digit of n
    pos_3 = k - 1
    # sign_sum  of the k_th block of three = (-1)^(k - 1)
    # the sign_sum of each block of 3 alternates from right to left
    sign_sum = 1
    for i in range(1,  n_blocks + 1):
        # print('abc = ', n[(pos_3 - 2): (pos_3 + 1)])
        # print('2.abc = '+ n[pos_3 - 2]+ n[pos_3 - 1]+ n[pos_3])
        alt_sum += sign_sum * \
                   ((2 * int(n[pos_3 - 2])
                     + 3 * int(n[pos_3 - 1])
                     + int(n[pos_3])) % 7)
        alt_sum = alt_sum % 7
        # the position of the last digit in the left next block of 3
        pos_3 = pos_3 - 3
        # alternate the sign
        sign_sum = sign_sum * (-1)
    print(f'\nRemainder of {int(n)} when dividing by 7 = ', alt_sum)
    return alt_sum == 0


if __name__ == '__main__':
    num = input('n = ')
    if divisible_by_seven(num):
        print('This number is divisible by 7.')
    else:
        print('This number is not divisible by 7.')
