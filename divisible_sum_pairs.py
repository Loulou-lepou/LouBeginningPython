# Daily challenge: https://ucode.vn/problems/94511?challenge-id=21
#  Inputs : 1 line contains 3 given integers A, B and K.
#  Constraints: 1 <= A, B, K <= 10^9
#  Output :  The number of pairs (x, y) satisfying
#             0 <= x <= A
#             0 <= y <= B
#             x + y = 0 (mod K)
# Sample test 1
# Input: 6 8 3
# output: 21
# 26/26 test cases passed ^^

# Step 1:  Get integers A, B, K from user inputs
A, B, K = map(int, input().split(' '))

# Step 2: [0, A] = [0, 1, 2, ..., K - 1],
#                  [K, K + 1, K + 2, ..., 2 * K - 1],
#               ...[K * (n_A - 1), K * (n_A - 1) + 1, ..., K * (n_A - 1) - 1],
#                  [k * n_A, ..., K * n_A + r_A - 1]
n_A, r_A = (A + 1) // K, (A + 1) % K
n_B, r_B = B // K, B % K
# Count # satisfied (x, y) where x in [0,..., K - 1]
# x = 0 -> y in multiples of K <= B => y in {0, K, 2 * K,..., K * t, K * n_B} => # (0, K*t) = n_B + 1
# x >= 1 => y in {K - x + K * t |  (K - x + K * t) <= B, t >= 0} =>  t <= (B + x) / K - 1
#  # (x, y) = floor(B + x / K) = n_B + floor((r_B + x) / K)
#  x < K - r_B => floor((r_B + x) / K ) = 0
#  K - r_B <= x <= K - 1  (number of such x = r_B) =>  K =< r_B + x <= 2 * (K - 1) => floor((r_B + x) / K) = 1
#  in [1, K - 1],  #(x, y) = n_B * (K - 1) + r_B
#  # satisfied (x, y) in [0,.., K - 1] = n_B  + 1 + [n_B * (K  - 1) + r_B ] = n_B * K + r_B + 1
count = n_B * K + r_B + 1
# # satisfied (x, y) in n_A sub-intervals : [K * t, ..., K * (t + 1) - 1]
count *= n_A

# [K * n_group, K * n_group + r_A - 1]
# [0, r_A - 1]
if r_A > 0:
    for x in range(0, r_A):
        if x == 0:
            count += n_B + 1
        else:
            count += n_B + (r_B + x) // K
print(count)
