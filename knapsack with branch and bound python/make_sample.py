
import numpy as np
from os import path
from sys import argv

def make_sample(weight, value, size_of_items,weight_of_knapsack):
    np.random.seed(0)
    _weight = np.random.randint(weight[0],weight[1], size_of_items)
    _value = np.random.randint(value[0], value[1], size_of_items)
    m = 1

    while True:
        file_path = path.join(path.dirname(__file__),"sample", f"{m}.txt")
        if path.exists(file_path):
            m += 1
        else:
            break

    with open(file_path, 'w') as f:
        f.write(f"{weight_of_knapsack} {size_of_items}\n")
        for i in zip(_weight, _value):
            f.write(f"{i[0]} {i[1]}\n")
    print(f"file {file_path} is created")

test_mode = False
if __name__ == "__main__":
    if test_mode:
        weight_of_knapsack = 10
        size_of_items = 140
        min_weight = 1
        max_weight = 10
        min_value = 10
        max_value = 50
    else:
        if len(argv) == 7:
            weight_of_knapsack = int(argv[1])
            size_of_items = int(argv[2])
            min_weight = int(argv[3])
            max_weight = int(argv[4])
            min_value = int(argv[5])
            max_value = int(argv[6])
        else:
            print("usage: python3 make_sample.py weight_of_knapsack size_of_items min_weight max_weight min_value max_value")
            exit()
    weight = (min_weight , max_weight)
    value = (min_value , max_value)

    make_sample(weight, value, size_of_items,weight_of_knapsack)
