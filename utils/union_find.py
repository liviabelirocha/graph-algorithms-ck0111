class UnionFind:
    def __init__(self, nodes):
        self.parent = list(range(len(nodes)))
        self.rank = list(range(len(nodes)))

        for node in nodes:
            # every node is its own parent
            self.parent[node] = node
            # every set contains only itself
            self.rank[node] = 1

    def find(self, x):
        # finds the root of the set
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # union by rank
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[y] = x
            self.rank[x] += 1