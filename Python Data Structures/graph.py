"""Name: Dustin Barnes
Class: 2400-001
Project 8: Graphs
All of the following code was written by me."""

class Graph:
    """Graph ADT allowing vertices and weighted edges
    to be added to the data structure. Also implements
    Dijkstra's shortest path algorithm to find the
    shortest path between two vertices."""
    def __init__(self):
        """Initiates the graph with an empty dictionary."""
        self.vertex_dict = {}

    def add_vertex(self, label):
        """Adds a vertex with no attached edges to the
        graph."""
        if not isinstance(label, str):
            raise ValueError("label must be a string")
        if label not in self.vertex_dict:
            self.vertex_dict[label] = []
        return self

    def add_edge(self, src, dest, w): #pylint: disable=C0103
        """Adds a weighted edge between two existing vertices."""
        if src not in self.vertex_dict:
            raise ValueError("src must be in the graph")
        if dest not in self.vertex_dict:
            raise ValueError("dest must be in the graph")
        if not isinstance(w, (float, int)):
            raise ValueError("w must be a float or an integer")
        if w < 0:
            raise ValueError("w must be a positive number")
        self.vertex_dict[src].append((dest, w))
        return self

    def get_weight(self, src, dest):
        """Gets the weight between two already existing vertices."""
        if src not in self.vertex_dict:
            raise ValueError("src must be in the graph")
        if dest not in self.vertex_dict:
            raise ValueError("dest must be in the graph")
        for vertex, weight in self.vertex_dict[src]:
            if vertex == dest:
                return weight
        return float('inf')

    def dfs(self, starting_vertex):
        """Implements a depth first search."""
        dfs_stack = [starting_vertex]
        dfs_visited_set = set()
        while len(dfs_stack) != 0:
            current_vertex = dfs_stack.pop()
            if current_vertex not in dfs_visited_set:
                yield current_vertex
                dfs_visited_set.add(current_vertex)
                for adj_vertex, _ in self.vertex_dict[current_vertex]:
                    dfs_stack.append(adj_vertex)

    def bfs(self, starting_vertex):
        """Implements a breadth first search."""
        bfs_queue = [starting_vertex]
        bfs_discovered_set = set(starting_vertex)
        while len(bfs_queue) != 0:
            current_vertex = bfs_queue.pop(0)
            yield current_vertex
            for adj_vertex, _ in self.vertex_dict[current_vertex]:
                if adj_vertex not in bfs_discovered_set:
                    bfs_queue.append(adj_vertex)
                    bfs_discovered_set.add(adj_vertex)

    def dijkstra_shortest_path(self, src, dest=None): #pylint: disable=R0912
        """Dijkstra's shortest path algorithm, can return either a
        dictionary with every vertex's distance from a source, or
        it can return a tuple with the shortest distance between
        a source and a destination along with the path taken between them."""
        if src not in self.vertex_dict:
            raise ValueError("src must be in the graph")
        if dest is not None and dest not in self.vertex_dict:
            raise ValueError("dest must be in the graph")
        distance_to_start = 0.0
        not_visited_list = [src]
        visited_list = []
        shortest_distance_dict = {}
        for item in self.vertex_dict:
            if item != src:
                shortest_distance_dict[item] = [float('inf'), []]
                not_visited_list.append(item)
            else:
                shortest_distance_dict[item] = [0.0, []]
        while len(not_visited_list) != 0:
            current_vertex = min(not_visited_list, key=(lambda x: shortest_distance_dict[x][0]))
            for adj_vertex, weight in self.vertex_dict[current_vertex]:
                if adj_vertex in not_visited_list:
                    distance_to_start = shortest_distance_dict[current_vertex][0] + weight
                    if distance_to_start < shortest_distance_dict[adj_vertex][0]:
                        shortest_distance_dict[adj_vertex][0] = distance_to_start
                        shortest_distance_dict[adj_vertex][1] = [current_vertex]
            visited_list.append(current_vertex)
            not_visited_list.remove(current_vertex)
        helper_shortest_dict = {}
        for item in shortest_distance_dict:
            helper_shortest_dict[item] = [shortest_distance_dict[item][0], shortest_distance_dict[item][1]] #pylint: disable=C0301
        for vertex in visited_list:
            path_list = []
            cursor = vertex
            while cursor != src:
                path_list.append(cursor)
                if len(shortest_distance_dict[cursor][1]) == 0:
                    break
                cursor = shortest_distance_dict[cursor][1][0]
            path_list.append(src)
            if helper_shortest_dict[vertex][0] != float('inf'):
                helper_shortest_dict[vertex][1] = path_list
        for item in helper_shortest_dict:
            shortest_distance_dict[item] = (helper_shortest_dict[item][0], helper_shortest_dict[item][1]) #pylint: disable=C0301
        if dest is None:
            return shortest_distance_dict
        return shortest_distance_dict[dest]

    def __str__(self):
        """String to be printed when the graph is printed."""
        return_str = f'numVertices: {len(self.vertex_dict)}\n'
        return_str += 'Vertex\tAdjacency List\n'
        for vertex in self.vertex_dict:
            return_str += f'{vertex}\t{self.vertex_dict[vertex]}\n'
        return return_str
