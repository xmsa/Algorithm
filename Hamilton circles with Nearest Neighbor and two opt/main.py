import Problem2
from sys import argv, exit
from Graph import Graph

def main(vertices, adj_mtx, verbose=False):
    if vertices is None:
        return None
    gragh = Graph(vertices, adj_mtx)
    path_obj = Problem2.Path(gragh)
    path = path_obj.Nearest_Neighbor()

    if verbose and path:
        print(" Nearest_Neighbor ".center(50, "-"))
        gragh.print_path(path)

    best_path = None
    if path:
        best_path = path_obj.two_opt(path)

    if verbose and path:
        print(" 2-Opt ".center(50, "-"))
        gragh.print_path(best_path)
    elif verbose:
        print("No path found")
    
    return gragh, path, best_path

test_mode = False
if __name__ == "__main__":
    if test_mode:
        file_path = "./sample/11.txt"
    else:
            
        if len(argv) == 2:
            parametr = argv[1]
        else:
            print("Usage: python3 main.py [file_name.txt]")
            print("Usage: python3 main.py [size of vertices]")
            exit()
    if parametr.isdigit():
        size_of_vertices = int(parametr)
        vertices, adj_mtx = Graph.read_input(size_of_vertices)
    else:
        file_path = parametr
        vertices, adj_mtx = Graph.read_txt(file_path)
    if vertices is None:
        exit()
    main(vertices, adj_mtx, verbose=True)
