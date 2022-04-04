# find min element in a list
# inputs:
# line 1: n = # list elements
# next n lines : list elements
# output: the minimum element in the list

def valid_positive_input():
    while True:
        try:
            user_input = int(input())
            if user_input > 0:
                break
            else:
                print("Ur number must be positive")
        except ValueError:
            print("Plz enter a real number")
    return user_input


def valid_float_input():
    while True:
        try:
            user_input = float(input())
            break
        except ValueError:
            print("Plz enter a real number")
    return user_input


def forming_list(num):
    return [valid_float_input() for _ in range(num)]


def find_min(list_):
    min_ = list_[0]
    for element in list_:
        if element < min_:
            min_ = element
    return min_


if __name__ == '__main__':
    num_element = valid_positive_input()
    my_list = forming_list(num_element)
    print(find_min(my_list))
