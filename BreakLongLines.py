#!usr/bin/env python3
# Ref : https://doingmathwithpython.github.io/breaking-long-lines-in-python.html

import math as m


def area_of_circle(radius):
    return m.pi * radius ** 2
# print(area_of_circle(3))


# Break the above long line by using extra beginning & ending parenthesis

# s = 'Area1 = {0}, Area2 = {1}'.format("%.4f"% area_of_circle(0.1), "%.4f" % area_of_circle(2))
s1 = ('Area1 = {0}, Area2 = {1}'
      .format("%.4f" % area_of_circle(0.1), "%.4f" % area_of_circle(2)))

s2 = 'Area1 = {0}, Area2 = {1}, Area3 = {2}'.format("%.4f" % area_of_circle(0.1),
                                                    "%.4f" % area_of_circle(2),
                                                    "%.4f" % area_of_circle(3))


def s3(x):
    # return x + x ** 2 / 2 + x ** 3 / 3 + x ** 4 / 4 + x ** 5 / 5 + x ** 6 / 6 + x ** 7 / 7 + x ** 8 / 8
    return (x + x ** 2 / 2 + x ** 3 / 3
            + x ** 4 / 4 + x ** 5 / 5
            + x ** 6 / 6 + x ** 7 / 7
            + x ** 8 / 8)


# Use the line continuation operator \

def s4(x):
    # return x + x ** 2 / 2 + x ** 3 / 3 + x ** 4 / 4 + x ** 5 / 5 + x ** 6 / 6 + x ** 7 / 7 + x ** 8 / 8
    return x + x ** 2 / 2 + x ** 3 / 3 \
           + x ** 4 / 4 + x ** 5 / 5 \
           + x ** 6 / 6 + x ** 7 / 7 \
           + x ** 8 / 8
