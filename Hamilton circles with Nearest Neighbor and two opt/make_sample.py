from os import path
import numpy as np
from Graph import Graph
from sys import argv

def make_sample(size_of_vertices, size_of_edges, cost=[1, 100]):
    vertices, adj_mtx = Graph.adjacency_matrix_generator(
        size_of_vertices, size_of_edges, cost)
    m = 1

    while True:
        file_path = path.join(path.dirname(__file__), "sample", f"{m}.txt")
        if path.exists(file_path):
            m += 1
        else:
            break
    vertices = list(map(str, vertices))
    with open(file_path, 'w') as f:
        f.write(f"{' '.join(vertices)}\n")
        for row in adj_mtx:
            _row = list(map(str, row))

            s = ' '.join(_row)
            f.write(f"{s}\n")
    print(f"file {file_path} is created")


test_mode = True
if __name__ == "__main__":
    if test_mode:
        make_sample(6,25)
    else:
        if len(argv) ] 2:
            if len(argv) == 5:
                make_sample(int(argv[1]), int(argv[2]), [int(argv[3]), int(argv[4])])
            elif len(argv) == 3:
                make_sample(int(argv[1]), int(argv[2]))
            elif len(argv) == 4:
                make_sample(int(argv[1]), int(argv[2]), [1, int(argv[3])])
            else:
                print("Invalid argument")
        else:
            print("Invalid argument")
            print("Usage: python3 make_sample.py [size_of_vertices] [size_of_edges] [cost_min] [cost_max]")
            print("Example: python3 make_sample.py 30 150 1 100")
