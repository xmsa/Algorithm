from backtracking import Backtracking
import sys


class Method:
    BACKTRACKING = 0


def main(size_of_board, method):
    if method is Method.BACKTRACKING:
        Backtracking(size=size_of_board).backtracking()


def print_doc():
    print("Using: python main.py method size_of_board")
    print("       method: 0-backtracking")


test_mode = False
if __name__ == "__main__":
    if test_mode:
        main(5, Method.BACKTRACKING)
        sys.exit()
    else:
        if len(sys.argv) == 3:
            if sys.argv[1] == "0":
                main(int(sys.argv[2]), Method.BACKTRACKING)
                sys.exit()
    print_doc()
