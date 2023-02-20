import numpy as np

class Graph:
    @staticmethod
    def adjacency_matrix_generator(size_of_vertices, size_of_edges, cost):
        size_of_edges = min((size_of_vertices*(size_of_vertices-1)), size_of_edges)//2
        vertices = list(range(size_of_vertices))
        adj_mtx = [[0]*size_of_vertices for i in range(size_of_vertices)]

        i = 0
        while i < size_of_vertices:
            c = np.random.choice(vertices, size=1, replace=False)[0]
            if c != i and adj_mtx[i][c] == 0:
                adj_mtx[i][c] = np.random.randint(cost[0], cost[1])
                adj_mtx[c][i]= adj_mtx[i][c]
                i+=1
        while i < size_of_edges:
            r, c = np.random.choice(vertices, size=2, replace=False)
            if adj_mtx[r][c] == 0:
                adj_mtx[r][c] = np.random.randint(cost[0], cost[1])
                adj_mtx[c][r] = adj_mtx[r][c]
                i += 1
        #         i+=1
        # r, c = np.random.choice(vertices, size=2, replace=False)
        vertices = [i+1 for i in vertices]
        return vertices, adj_mtx
    @staticmethod
    def adjacency_matrix_generator_str(size_of_vertices, size_of_edges, cost):
        vertices, adj_mtx = Graph.adjacency_matrix_generator(size_of_vertices, size_of_edges, cost)
        vertices = list(map(str, vertices))
        adj_mtx = [list(map(str, row)) for row in adj_mtx]
        return [" ".join(vertices)] + [" ".join(row) for row in adj_mtx]