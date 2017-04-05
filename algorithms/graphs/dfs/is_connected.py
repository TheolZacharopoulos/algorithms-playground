from algorithms.graphs.SimpleGraph import Graph

"""
Undirected:
We can use the basic DFS function to determine whether a graph is connected.
In the case of an undirected graph, we simply start a depth-first search at an arbitrary vertex
and then test whether len(discovered) equals n at the conclusion.

If the graph is connected, then all vertices will have been discovered; conversely, if the graph is not connected,
there must be at least one vertex v that is not reachable from u, and that will not be discovered.
"""


def dfs_explore(graph, source):
    visited = []
    stack = [source]

    while stack:
        v = stack.pop()

        if v in visited:
            continue

        visited.append(v)

        for n in graph.incident_edges(v):
            stack.append(n)

    return visited


def is_connected(graph, source):
    discovered = dfs_explore(graph, source)
    all_vertices = graph.vertices()
    return len(discovered) == len(all_vertices)


if __name__ == "__main__":
    g = Graph()

    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('E')
    g.add_vertex('F') # F is not connected
    g.add_vertex('I')
    g.add_vertex('J')

    g.add_edge('A', 'B')
    g.add_edge('A', 'E')

    g.add_edge('E', 'A')
    g.add_edge('E', 'I')

    g.add_edge('I', 'E')
    g.add_edge('I', 'J')

    g.add_edge('J', 'E')
    g.add_edge('J', 'I')

    print(is_connected(g, 'A'))

    g_2 = Graph()

    g_2.add_vertex('A')
    g_2.add_vertex('B')
    g_2.add_vertex('C')
    g_2.add_vertex('D')

    g_2.add_edge('A', 'B')
    g_2.add_edge('B', 'C')
    g_2.add_edge('B', 'D')
    print(is_connected(g_2, 'A'))
