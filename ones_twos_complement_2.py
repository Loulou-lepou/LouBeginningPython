def flip(c):
    return '1' if (c == '0') else '0'
def ones_twos_complement(bin_str):
    n = len(bin_str)
    ones, twos = "", list(bin_str)
    # for 1's complement, flip every bit
    for _ in range(n):
        ones += flip(bin_str[_])
    # for 2's complement, go from right to left until we find 1
    # keep that 1 & flip all the bits
    i = 0
    for i in range(n - 1, -1, -1):
        if bin_str[i] == '1':  # ones[i] = 0
            break
    # no break (i = -1), i.e bin = "0...0" (all are 0)
    # add extra 1 at beginning
    if i > 0:
        for j in range(i):
            twos[j] = ones[j]
    else:
        twos[0] = '1'
    return ones, ''.join(twos)
print(ones_twos_complement("100100"))
print(ones_twos_complement("00000000"))
