# Given a number n, determine if n is divisible by 7.
# (Thanks Nghi Nguyen - my mentor for his contribution)


def divisible_by_seven(n: str) -> bool:
    # 10^k mod 7 repeatS in a cycle of [1, 3, 2, -1, -3, -2]
    # = [10^0, 10^1, 10^2, 10^3, 10^4, 10^5] mod 7
    pow10s = [1, 3, 2, -1, -3, -2]
    total = 0
    k = len(n)
    pos = k - 1
    i_10 = 0
    for i in range(pos, -1, - 1):
        total = (total + (int(n[i]) * pow10s[i_10]) % 7) % 7
        # print('{0} {1} {2} {3}'.format(i, n[i], total, i_10))
        i_10 = (i_10 + 1) % 6
    print(f'Remainder of {int(n)} when dividing by 7 = {total}')
    return total == 0


if __name__ == '__main__':
    # ['8638', '21', '15935746258', '123456789', '1369851', '483']
    user_list = input('Enter elements of a list separated by space').split(' ')
    for num in user_list:
        if divisible_by_seven(num):
            print('{0} is divisible by 7'.format(num))
        else:
            print('{0} is NOT divisible by 7'.format(num))
        print('=============================')
