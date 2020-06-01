#!/usr/bin/env python3
# Find maximum and minimum of an array - Simple Linear Search
# Time complexity : O(n)


def get_min_max(arr: list):

    if len(arr) == 1:
        return arr[0], arr[0]

    if arr[0] > arr[1]:
        e_min, e_max = arr[1], arr[0]
    else:
        e_min, e_max = arr[0], arr[1]

    for i in range(2, len(arr)):
        if arr[i] > e_max:
            e_max = arr[i]
        elif arr[i] < e_min:
            e_min = arr[i]

    return e_min, e_max


if __name__ == '__main__':
    L = [1000, 11, 445, 1, 330, 3000]
    (min_element, max_element) = get_min_max(L)
    print("Minimum element is ", min_element)
    print("Maximum element is ", max_element)
