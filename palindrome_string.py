""" test a given string is a palindrome (after removing special symbols) """


class Solution:
    """ solutions """
    @staticmethod
    def isPalindrome(string_):
        """ test a given string is a palindrome (after removing special symbols)"""
        stripped_str = string_.strip()
        # remove special symbols '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        non_blank_characters = [char.lower() for char in stripped_str if char.isalnum()]
        num_characters = len(non_blank_characters)
        for index in range(num_characters // 2 + 1):
            if non_blank_characters[index] != non_blank_characters[num_characters - index - 1]:
                return 0
        return 1


if __name__ == '__main__':
    num_testcases = int(input())
    for _ in range(num_testcases):
        input_str = input()
        ob = Solution()
        answer = ob.isPalindrome(input_str)
        print(answer)
