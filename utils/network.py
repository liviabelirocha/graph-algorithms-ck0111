from .graph import Graph

class Network(Graph):
    def change_weight(self, node1, node2, weight):
        updated = False
        for i, (n, w) in enumerate(self._graph[node1]):
            if n == node2:
                self._graph[node1][i] = (node2, weight)
                updated = True
                break

        if not self._directed:
            for i, (n, w) in enumerate(self._graph[node2]):
                if n == node1:
                    self._graph[node2][i] = (node1, weight)
                    updated = True
                    break

        if not updated:
            self.add(node1, node2, weight)
            self._edges.append([node1, node2, weight])