# Ref link :
# https://quantrimang.com/hon-100-bai-tap-python-co-loi-giai-code-mau-142456#mcetoc_1btli9vou0
# https://github.com/Loulou-lepou/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises%20for%20Python%203.md

# Python_Level1_E1
# Find all numbers that are divisible by 7 but not divisible by 5
# and belong to the closed interval [2000, 3200].
# The numbers obtained should be printed in a comma - separated sequence on a single line.

# Method 1
cnt = 0
for i in range(2000, 3200 + 1):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=',')
        cnt += 1
print('\n', cnt)
# returns 2002,2009,2016,.....,3199,
# the ending comma is undesired

# Method 2
j = []        # initialize an empty list
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
        # list append() method : list.append(elmnt)
        # appends an elmnt to the end of the list
# j = list of strings
print(','.join(j))
# Python string join method :
# separator_str.join(iterable_of_str)
# join() method takes all items from the iterable_of_str and joins them into 1 string
print(len(j))
