# built-in module containing methods for interacting with the operating system
import os


def absolute_path():
    # backward slash \ -> escape character  (e.g: \n, \t)
    # Method 1 : specify the file path using forward slash /
    # using the absolute path    -> system dependent
    # absolute_file_path = "C:/Users/Admin/PycharmProjects/NewLoulou2021/Fundamental Python June 2021/LU_Week_7/ex1.txt"
    # file_name = absolute_file_path.split("/")[-1]
    # Method 2: specify the file path using two backward slashes \\
    # file_path = "C:\\Users\\Admin\\PycharmProjects\\NewLoulou2021\\Fundamental Python June 2021\\LU_Week_7\\ex1.txt"
    # file_name = file_path.split("\\")[-1]
    # print("the working file:", file_name)
    # Method 3: specify the file path using raw string:
    absolute_file_path = r"C:\Users\Admin\PycharmProjects\NewLoulou2021\Fundamental Python June 2021\LU_Week_7\ex1.txt"
    # use relative file path
    return absolute_file_path


def relative_path():
    # using the relative path
    file_path_2 = "ex3.txt"
    return file_path_2


def open_files(file_path):
    # check if the file exists
    try:
        os.path.isfile(file_path)
        file = open(file_path, "r")
        # result: 'John\nYinuo\nPekka\nDieter\nJanis\nSandor\n'
        # contents = file.read()
        contents = file.read(10)
        print(contents)
        file.close()
    except FileNotFoundError:
        print("Invalid file path, plz enter a correct file path")


def with_open_file(file_path):
    # after excecuting the code within the block
    # 'with' statement will automatically close the file
    with open(file_path, "r") as file:
        # a single string joining all lines with delimiter \n
        contents = file.read()
        # contents = file.read(10)
    print(contents)


def characters_encodings(file_path):

    # UnicodeEncodeError: 'charmap' codec can't encode character '\u0394
    # ' in position 25: character maps to <undefined>
    # with open(file_path, "w") as file:
    #    file.write("with Unicode characters: Δv / Δt")

    # avoid the UnicodeEncodeError:
    with open(file_path, "w", encoding="utf-8", errors="ignore") as file:
        file.write("with Unicode characters: Δv / Δt")


if __name__ == '__main__':
    open_files(absolute_path())
    with_open_file(relative_path())
    characters_encodings("Loulou1.txt")
    open_files(input('Enter a relative file path: '))
