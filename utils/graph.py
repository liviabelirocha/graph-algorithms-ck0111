from collections import defaultdict

class Graph():
    def __init__(self, connections=[], directed=False):
        self._graph = defaultdict(list)
        self._edges = []
        self._directed = directed
        self._vertices = []
        self.add_connections(connections)

    def add_connections(self, connections):
        for connection in connections:
            node1 = connection[0]
            node2 = connection[1] if len(connection) > 1 else None
            weight = connection[2] if len(connection) > 2 else None

            if node1 not in self._vertices:
                self._vertices.append(node1)
            if node2 not in self._vertices:
                self._vertices.append(node2)

            if (node2):
                self.add(node1, node2, weight)
                self._edges.append([node1, node2, weight])
            else:
                self._graph[node1]

    def add(self, node1, node2, weight=1):
        self._graph[node1].append((node2, weight))

        if not self._directed:
            self._graph[node2].append((node1, weight))

    def sort(self):
        return sorted(self._edges, key=lambda x: x[2])
    
    def V(self):
        return len(self._vertices)
    
    def get_weight(self, u, v):
        for vertix, weight in self._graph[u]:
            if vertix == v:
                return weight
        return 0

    def __str__(self):
        return f'{self.__class__.__name__} ({dict(self._graph)})'