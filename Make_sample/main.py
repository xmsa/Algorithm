import sys
import os
import numpy as np
from binery_search_sample import Binary_Search_Sample


class Method:
    BINERY_SEARCH = 0
    Method = {0: "binery_search"}


def make_sample(**kwarg):
    if kwarg["method"] == Method.BINERY_SEARCH:
        out = Binary_Search_Sample.make_sample_with_str(
            kwarg["size"], kwarg["min"], kwarg["max"])

    path = "./sample"
    if not os.path.exists(path):
        os.mkdir(path)
        print("mkdir sample")
    counter = 1
    method_name = Method.Method[kwarg["method"]]
    while True:
        file_path = os.path.join(path, f"{method_name}{counter}.txt")
        if not os.path.exists(file_path):
            break
        counter += 1

    with open(file_path, "w") as f:
        for line in out:
            f.writelines(line+"\n")
    print(f"savefile:{file_path}")


def print_doc():
    print("Err")
    print("Using: python main.py method_number Args")
    print("for Binery search sample: 0 size min max")


test_mode = False
if __name__ == "__main__":
    if test_mode:
        make_sample(method=Method.BINERY_SEARCH, size=10, min=0, max=100)
        sys.exit()

    if len(sys.argv) > 2:
        method = int(sys.argv[1])
        if method == Method.BINERY_SEARCH:
            size = int(sys.argv[2])
            min_ = int(sys.argv[3])
            max_ = int(sys.argv[4])
            make_sample(method=method, size=size, min=min_, max=max_)
            exit()
    print_doc()
