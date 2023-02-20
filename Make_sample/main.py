import sys
import os
import numpy as np
from binery_search_sample import Binary_Search_Sample
from adjacency_matrix_graph import Graph
from knapsack_sample import Knapsack_Sample


class Method:
    BINERY_SEARCH = 0
    ADJACENCY_MATRIX = 1
    KNAPSACK = 2
    Method = ["binery_search", "adjacency_matrix", "knapsack"]


def make_sample(**kwarg):
    if kwarg["method"] == Method.BINERY_SEARCH:
        out = Binary_Search_Sample.make_sample_with_str(
            kwarg["size"], kwarg["min"], kwarg["max"])
    elif kwarg["method"] == Method.ADJACENCY_MATRIX:
        out = Graph.adjacency_matrix_generator_str(kwarg["size_of_vertices"],
                                                   kwarg["size_of_edges"], kwarg["cost"])
    elif kwarg["method"] == Method.KNAPSACK:
        out = Knapsack_Sample.Knapsack_generator_str(
            value=kwarg["value"],
            weight=kwarg["weight"],
            size_of_items=kwarg["size_of_items"],
            weight_of_knapsack=kwarg["weight_of_knapsack"]
        )

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
    print("for Adjacency Matrix sample: 1 sizeOfVertices sizeOfEdges min_Cost maxCost")
    print("Knapsack :2 weight_of_knapsack size_of_items min_weight max_weight min_value max_value")


test_mode = False
if __name__ == "__main__":
    if test_mode:
        # make_sample(method=Method.BINERY_SEARCH, size=10, min=0, max=100)
        # make_sample(method=Method.ADJACENCY_MATRIX,
        #             size_of_vertices=10, size_of_edges=20, cost=[1, 100])
        make_sample(method=Method.KNAPSACK,
                    value=[5, 100],
                    weight=[10, 1000],
                    size_of_items=5,
                    weight_of_knapsack=4
                    )

        sys.exit()

    if len(sys.argv) > 2:
        method = int(sys.argv[1])
        if method == Method.BINERY_SEARCH:
            if len(sys.argv) == 5:
                size = int(sys.argv[2])
                min_ = int(sys.argv[3])
                max_ = int(sys.argv[4])
                make_sample(method=method, size=size,
                            min=min_, max=max_)
                exit()
        elif method == Method.ADJACENCY_MATRIX:
            if len(sys.argv) == 6:
                size_of_vertices = int(sys.argv[2])
                size_of_edges = int(sys.argv[3])
                cost = [int(sys.argv[4]), int(sys.argv[5])]
                make_sample(method=method, size_of_vertices=size_of_vertices,
                            size_of_edges=size_of_edges, cost=cost)
                exit()
        elif method == Method.KNAPSACK:
            if len(sys.argv) == 8:
                weight_of_knapsack = int(sys.argv[2])
                size_of_items = int(sys.argv[3])
                min_weight = int(sys.argv[4])
                max_weight = int(sys.argv[5])
                min_value = int(sys.argv[6])
                max_value = int(sys.argv[7])
                make_sample(method=method,
                            weight_of_knapsack=weight_of_knapsack,
                            size_of_items=size_of_items,
                            weight=[min_weight, max_weight],
                            value=[min_value, max_value])
                exit()

    print_doc()
