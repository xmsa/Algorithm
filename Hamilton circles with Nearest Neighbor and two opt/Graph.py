import numpy as np

class Graph:
    def __init__(self, vertices, adj_mtx):
        self.__vertices = vertices
        self.__adj_mtx = adj_mtx
        self.__graph = self.__convert()
        self.__size_of_vertices = len(self.__vertices)
        self.__size_of_edges = 0
        for key in self.__graph:
            self.__size_of_edges += len(self.__graph[key])

    def __convert(self):
        graph = dict()
        for i in self.__vertices:
            graph[i] = list()
        for i in range(len(self.__vertices)):
            for j in range(len(self.__vertices)):
                if self.__adj_mtx[i][j] == 0:
                    continue
                graph[self.__vertices[i]].append(
                    [self.__vertices[j], self.__adj_mtx[i][j]])
        return graph

    def __getitem__(self, key):
        return self.__graph[key]

    def __setitem__(self, key, value):
        self.__graph[key] = value

    def __str__(self):
        return str(self.__graph)

    @property
    def vertices(self):
        return self.__vertices

    @property
    def legth(self):
        return self.__size_of_vertices, self.__size_of_edges

    def neighbor(self, vertices):
        ''' return list of neighbor vertices'''
        if vertices in self.__vertices:
            return [v[0] for v in self.__graph[vertices]]
        else:
            return None

    def chack_path(self, path):
        ''' return True if path is valid, else return False'''
        if path is None:
            return False
        for i in range(len(path)-1):
            if path[i+1] not in self.neighbor(path[i]):
                return False
        return True

    def cost_path(self, path):
        ''' return total cost of path'''
        if not self.chack_path(path):
            return None
        cost = 0

        for i in range(len(path)-1):
            neighbor = self.neighbor(path[i])
            index = neighbor.index(path[i+1])
            cost += self.__graph[path[i]][index][1]
        return cost

    @staticmethod
    def read_txt(file_path):
        try:
            with open(file_path, "r") as f:
                vertices = f.readline().strip().split(" ")
                adj_mtx = list()
                for line in f:
                    if line.strip() == "":
                        continue
                    adj_mtx.append(list(map(int, line.strip().split(" "))))
            return vertices, adj_mtx
        except:
            print("Can't read file")
            return None, None

    @staticmethod
    def read_input(size_of_vertices):
        print("Enter adjacency matrix: ")
        adj_mtx = list()
        
        while len(adj_mtx) < size_of_vertices:
            
            row = input(f"row {len(adj_mtx)+1}: ").split()
            if len(row) != size_of_vertices:
                print("Invalid input")
                continue
            adj_mtx.append(list(map(int, row)))
        return vertices, adj_mtx

    def print_path(self, path):
        ''' print path'''
        print("path: ", end="")
        print(*path, sep="-")
        print("Total Cost: ", self.cost_path(path))

