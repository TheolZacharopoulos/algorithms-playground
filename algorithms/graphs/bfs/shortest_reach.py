# https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach
import operator


class Graph:
    def __init__(self, num):
        self._adjacency_map = {}
        for i in range(1, num + 1):
            self._adjacency_map[i] = []

    def connect(self, v, u):
        # since it is undirected
        self._adjacency_map[v].append(u)
        self._adjacency_map[u].append(v)

    def _find_distances(self, start):
        dist = {}
        for u in self._adjacency_map.keys():
            dist[u] = -1

        queue = [s]
        dist[start] = 0

        while queue:
            v = queue.pop(0)

            for u in self._adjacency_map[v]:
                if dist[u] == -1:
                    queue.append(u)
                    dist[u] = dist[v] + 1
        return dist

    def find_all_distances(self, start):
        dist = self._find_distances(start)

        sorted_dist = sorted(dist.items(), key=operator.itemgetter(0))

        for node, distance in sorted_dist:
            if distance < 0:
                print(str(distance) + " ", end='')
            if distance > 0:
                print(str(distance * 6) + " ", end='')
        print("")


q = int(input())

for _ in range(q):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)

    for _ in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x, y)

    s = int(input())
    graph.find_all_distances(s)

