"""
take a string containing punctuation characters as an input
remove all punctuation characters from it,
then print both the original string and the modified string to the console.
"""
import string


def punctuated_str():
    """ ask for a string that contains some punctuation character(s) """
    while True:
        input_str = input("Enter a string that contains punctuation characters:\n")
        if input_str.isalnum():
            print("The string should contain some punctuation character.")
        else:
            return input_str


def remove_punctuation(punctuated_str_input):
    """ remove punctuation(s) from the punctuated string"""
    punctuation_list = set()
    modified_str = ''
    # use .isalnum() -> check over a set of alphabets and digits
    # for char in punctuated_str_input:
    #     if char.isalnum():
    #         modified_str += char
    #     elif char != ' ':
    #         punctuation_list.add(char)

    # use string.punctuation -> check over a set with lesser elements (better)
    for char in punctuated_str_input:
        if char in string.punctuation:
            punctuation_list.add(char)
        else:
            modified_str += char

    print("The original string: '{}'".format(punctuated_str_input))
    print("The modified string: '{}'".format(modified_str))
    ans = "have" if len(punctuation_list) >= 2 else "has"
    print(punctuation_list, ans, "been removed.")


input_string = punctuated_str()
remove_punctuation(input_string)

