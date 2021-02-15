# Ref : https://www.geeksforgeeks.org/python-program-to-covert-decimal-to-binary-number/


# Method 1 : Recursive solution
def decimal_to_binary(int_num: int):                  # int_num must be an integer
    if int_num >= 1:
        decimal_to_binary(int_num // 2)               # successive division
        print(int_num % 2, end='')                    # print remainders in reverse order


# Method 2: Using built-in function bin
def decimal_to_binary2(int_num):
    return bin(int_num).replace("0b", "")
    # bin() => convert an integer into the binary format string prefixed with "0b"
    # run bin() function with a float argument
    # => TypeError: 'float' object cannot be interpreted as an integer


# Driver code
if __name__ == '__main__':

    dec_val = 29
    print("convert " + str(dec_val) + "to binary :", end='')
    decimal_to_binary(dec_val)
    print('\n')

    dec_val2 = 47
    print("convert " + str(dec_val2) + "to binary :" + decimal_to_binary2(dec_val2))
