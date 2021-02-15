# Done https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/
# https://www.stem.org.uk/resources/elibrary/resource/421210/floating-point-binary-representation-worksheet
# https://www.stem.org.uk/system/files/elibrary-resources/legacy_files_migrated/25265-unplugged-01-binary_numbers.pdf
# https://www.stem.org.uk/system/files/elibrary-resources/legacy_files_migrated/25266-unplugged-02-image_representation.pdf
# .https://www.quora.com/Why-is-the-largest-single-precision-IEEE-754-binary-floating-point-number-2%E2%88%922-%E2%88%9223-%C3%97-2-127
# .https://www.electronics-tutorials.ws/binary/binary-fractions.html
# .https://www.youtube.com/watch?v=tx-M_rqhuUA (convert decimal to IEEE 754 single precision binary)
# .https://www.youtube.com/watch?v=iTdpl-FZD0o (Visual proof : sum of infinite series)
import bitstring


def decimal_to_binary(n: int):
    if n > 1:
        decimal_to_binary(n//2)
    print(n % 2, end="")


def binary_to_decimal(binary_number):
    binary1 = binary_number
    decimal = 0
    i = 0
    while binary1 != 0:
        decimal = decimal + (binary1 % 10) * pow(2, i)
        binary1 = binary1 // 10
        i += 1
    print(decimal)


def string_binary_to_decimal(input_string):
    dec = 0
    for i in range(len(input_string) - 1, -1, -1):
        dec = dec + int(input_string[i]) * pow(2, len(input_string) - 1 - i)
    return print(dec)


if __name__ == '__main__':

    print("print(\"{0:b}\".format(9)) = ", "{0:b}".format(9))
    print("print(\"{:07b}\".format(2 ** 6 - 1)) = ", "{:07b}".format(2 ** 6 - 1))
    print("print(int(\'111\',2)) =", int('111', 2))
    print("print(0b1111) =", 0b1111)

    print("decimal_to_binary(2 ** 6 - 1) = ", end="")
    decimal_to_binary(2 ** 6 - 1)

    print("\n", len('111111'))
    print("")
    print("bin(8).replace(\"0b\", \"\") =", bin(8).replace("0b", ""))

    print("binary_to_decimal(111) = ", end="")
    binary_to_decimal(111)

    print("string_binary_to_decimal('011111111') = ", end="")
    string_binary_to_decimal('01111111')

    f1 = bitstring.BitArray(float=1/4, length=32)
    print(f1.bin)
    print(bitstring.BitArray(float=1/3, length=32).bin)
