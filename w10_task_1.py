"""
1. write a function input_integer()
- validate an input integer -> ValueError

"""


def input_integer():
    """ validate an input integer """
    try:
        input_num = int(input("Enter an integer:\n"))
        return input_num
    except ValueError:
        print("Invalid input. Please enter an integer.")


if __name__ == '__main__':
    num_inputs = input_integer()
    print("Now give {} integers!".format(num_inputs))
    sum_ = 0
    count = 0
    while count < num_inputs:
        term = input_integer()
        # if term != None:  => comparison with None performed with equality operators
        if term is not None:
            sum_ += term
            count += 1
    print("The sum of the entered integers is:", sum_)
