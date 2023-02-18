from node import node
from sys import argv
import os
import Problem1

test_mode = False
items = None 
weight_of_knapsack = None

if __name__ == "__main__":
    if test_mode:
        items, weight_of_knapsack = Problem1.Knapsack.read_txt("./sample/1.txt")
    else:
        if len(argv) == 2:
            items, weight_of_knapsack = Problem1.Knapsack.read_txt(argv[1])
        if len(argv) == 3:
            weight_of_knapsack, size_of_items = int(argv[1]), int(argv[2])
            items, weight_of_knapsack = Problem1.Knapsack.read_input(
                weight_of_knapsack, size_of_items)
    
    if items is None or weight_of_knapsack is None:
        print("Invalid input")
        print("Usage: python3 main.py [input_file_path]")
        print("Usage: python3 main.py [weight_of_knapsack] [size_of_items]")
        exit()
        
    k = Problem1.Knapsack(items)
    k.print()
    _node = k.knapsack(weight_of_knapsack, 0)
    print(" Problem 'A' ".center(50,'*'))
    _node.print(items)
    _node = k.knapsack(weight_of_knapsack, 1)
    print(" Problem 'B' ".center(50, '*'))
    _node.print(items)
