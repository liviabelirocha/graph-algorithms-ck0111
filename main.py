from utils.graph import Graph

if __name__ == '__main__':
    connections = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'), ('F', 'C')]
    graph = Graph(connections)
    print(graph)
    