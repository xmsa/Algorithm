import sys
import os
from binary_search import Binary_Search


def read_file(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            str_ = f.readline()
            str_.strip()
            lst = str_.split(",")
            lst = list(map(float, lst))
        return lst
    else:
        print("File does not exist")


def read_input(size_of_list):
    lst = []
    n = 0
    while n < size_of_list:
        try:
            inp = float(input(f"Enter the element {n+1}: "))
            lst.append(inp)
            n += 1
        except ValueError:
            print("eroor value")
            continue
        except KeyboardInterrupt:
            sys.exit()
    return lst


class Method:
    NON_RECERCIVE = 0
    RECERCIVE = 1


def print_doc():
    print("Err")
    print("Usage: python main.py [method] [value] [method_input]")
    print("method: 0 - non-recursive")
    print("        1 - recursive")
    print("value: int, float, ...")
    print("method_input: if Number -> input from console")
    print("              if file -> path to file")


def main(lst, value, method):
    print(lst)
    if lst is None:
        print_doc()
        return
    if method == Method.RECERCIVE:
        print(Binary_Search.binary_search(lst, value, recursive=True))
    elif method == Method.NON_RECERCIVE:
        print(Binary_Search.binary_search(lst, value, recursive=False))
    else:
        print_doc()


if __name__ == "__main__":
    test_mode = False
    if test_mode:
        # lst = read_file("./sample/binery_search3.txt")
        lst = read_input(5)
        method = Method.NON_RECERCIVE
        value = 4.13
        main(lst, value, method)
    else:
        if len(sys.argv) == 4:
            method = int(sys.argv[1])
            value = float(sys.argv[2])

            if sys.argv[3].isdigit():
                lst = read_input(int(sys.argv[3]))
            else:
                lst = read_file(sys.argv[3])
            main(lst, value, method)
        else:
            print_doc()
