class Solution:
    def getNumber(self, base, decimal_num):
        symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                   'A', 'B', 'C', 'D', 'E', 'F']
        quotient = decimal_num // base
        remainder = decimal_num % base
        result = [symbols[remainder]]
        while quotient != 0:
            decimal_num = quotient
            quotient = decimal_num // base
            remainder = decimal_num % base
            result.append(symbols[remainder])
        # read the remainders in a reversed order
        return ''.join(result[::-1])


if __name__ == '__main__':
    num_test_cases = int(input("Enter the number of test cases: "))
    for _ in range(num_test_cases):
        base_num = int(input("Enter the base: "))
        num = int(input("Enter the decimal number: "))
        ob = Solution()
        ans = ob.getNumber(base_num, num)
        print(f"{num} can be converted to base {base_num} as {ans}")
