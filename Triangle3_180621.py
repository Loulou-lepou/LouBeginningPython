# https://ucode.vn/problems/triangle-44815
# Input: a unique line consists of 3 positive integers a, b and c.
# = 3 sides of a triangle.
# Output : a unique real number S = the area of the triangle, rounding off to 2 decimal places.
# print out -1.00 if the triangle does not exist.

import math as m


list1 = input().split(" ")
a, b, c = [int(list1[i]) for i in range(3)]

S = -1.00
if a + b > c and a + c > b and b + c > a:  # triangle inequalities
    p = (a + b + c) / 2                    # semi-perimeter
    S = m.sqrt(p * (p - a) * (p - b) * (p - c))  # Heron's formula

print("{:.2f}".format(S))

# https://pythonguides.com/python-print-2-decimal-places/
