# 28/1/2020
# Linear/ Sequential Search  - Basic algorithm
# A linear search sequentially checks each element of the list
# until it finds an element that marches the target value.
# If the algorithm reaches the end of the list, the search terminates unsuccessfully.
#
# Time complexity O(n).
# Linear search is rarely used practically because other search algorithms such as
# the binary search algorithm and hash tables allow significantly faster searching comparison to Linear search.


def enter_int():
    while True:
        try:
            n_elements = int(input("Number of elements = "))
            break
        except ValueError:
            print('Plz enter a valid integer number')

    return n_elements


def enter_float():
    while True:
        try:
            t = float(input(""))
            break
        except ValueError:
            print("Plz enter the valid float number")

    return t


def enter_float_list(number_elements):
    list1 = []
    print("Enter " + str(number_elements) + " float elements ")

    for i in range(number_elements):
        # list1.append(int(input("L[" + str(i) + "] = ")))
        list1_i = enter_float()
        list1.append(list1_i)

    return list1
    # display the list in a nicer format - it might lead to rounding off error while searching
    # print("L = [" + str("%.3f, " * (len(list1) - 1) + "%.3f") % tuple(list1) + "]")


def float_list2():
    input_string = input("\nEnter the list numbers separated by space: ")
    list2 = []
    for num in input_string.strip().split():
        list2.append(float(num))

    return list2


def my_linear_search(l, t):
    s = 0
    for i in range(len(l)):
        if l[i] == t:
            print("Element is present at index " + str(i), end="")
            s = 1
            break

    if s == 0:
        print("The search terminates unsuccessfully. The element is not present in the given list")


if __name__ == '__main__':
    n = enter_int()
    my_list = enter_float_list(n)
    print("l = ", my_list, end="")
    print("\nenter the target value = ", end="")
    target_value = enter_float()
    my_linear_search(my_list, target_value)

    user_list = float_list2()
    print("new list = ", user_list, "\nnew target value = ", end="")
    new_target_value = enter_float()
    my_linear_search(user_list, new_target_value)
