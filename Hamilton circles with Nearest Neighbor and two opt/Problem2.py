class Path:
    def __init__(self, graph):
        self.__graph = graph
        self.__path = None

    @property
    def path(self):
        return self.__path

    def Nearest_Neighbor(self, start=None):
        ''' return path using Nearest Neighbor algorithm'''
        # Initialization
        path = list()
        if start:
            vertex = start
        else:
            vertex = self.__graph.vertices[0]
        visited = set()
        path = self.__Nearest_Neighbor(path, visited, vertex)
        if path:
            self.__path = path
            return self.path
        else:
            return None

    def __Nearest_Neighbor(self, path, visited, vertex):
        ''' return path using Nearest Neighbor algorithm'''
        visited.add(vertex)
        path.append(vertex)
        neighbor = self.__graph.neighbor(vertex)
        if len(visited) == len(self.__graph.vertices):
            if path[0] in neighbor:
                path.append(path[0])
                return path
            return None
        if not neighbor:
            return None
        neighbor.sort(key=lambda v: self.__graph.cost_path([vertex, v]))
        for ver in neighbor:
            if ver in visited:
                continue
            new_path = self.__Nearest_Neighbor(
                path.copy(), visited.copy(), ver)
            if new_path:
                return new_path
    def two_opt(self, path=None):
        ''' return path using 2-opt algorithm'''

        if path is None:
            if self.__path is None:
                path = self.Nearest_Neighbor()
            else:
                path = self.path
        found_best_path = True
        while found_best_path:
            path, found_best_path = self.__two_opt(path)
        self.__path = path
        return path

    def __two_opt(self, path):
        try:
            found_best_path = False
            cost_path = self.__graph.cost_path(path)
            for i in range(1, len(path)-2):
                for j in range(i+1, len(path)-1):
                    # check if swap is better
                    new_path = path[:i] + path[i:j + 1][::-1] + path[j + 1:]
                    cost_new_path = self.__graph.cost_path(new_path)
                    if cost_new_path:
                        if cost_path > cost_new_path:
                            path = new_path
                            found_best_path = True

            return path, found_best_path
        except:
            return path, False
