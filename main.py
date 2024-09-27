from algorithms.kruskal import kruskal
from algorithms.prim import prim
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.dijkstra import dijkstra
from algorithms.bellman_ford import bellman_ford
from algorithms.ford_fulkerson import ford_fulkerson

if __name__ == '__main__':
    # connections = [(0, 1, 4), (0, 7, 8), 
    #                (1, 2, 8), (1, 7, 11),
    #                (2, 3, 7), (2, 8, 2), (2, 5, 4),
    #                (3, 4, 9), (3, 5, 14),
    #                (4, 5, 10),
    #                (5, 6, 2),
    #                (6, 7, 1), (6, 8, 6),
    #                (7, 8, 7)]

    # connections = [('LIVRO', 'LP', 5), ('LIVRO', 'POSTER', 0),
    #                ('LP', 'BAIXO', 15), ('LP', 'BATERIA', 20), ('LP', 'POSTER', -7),
    #                ('POSTER', 'BAIXO', 30), ('POSTER', 'BATERIA', 35), ('POSTER', 'LP', -7),
    #                ('BAIXO', 'PIANO', 20),
    #                ('BATERIA', 'PIANO', 10)]

    # connections = [(0, 1, 16), (0, 2, 13),
    #                (1, 2, 10), (1, 3, 12),
    #                (2, 1, 4), (2, 4, 14),
    #                (3, 2, 9), (3, 5, 20),
    #                (4, 3, 7), (4, 5, 4)]

    connections = [('A', 'B', 4), ('A', 'C', 1),
                   ('B', 'D', 3),
                   ('C', 'B', -2)]

    dijkstra(connections, 'A')    