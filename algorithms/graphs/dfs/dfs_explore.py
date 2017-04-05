from algorithms.graphs.SimpleGraph import Graph


def dfs_explore_rec(graph, source, visited=None):
    if visited is None:
        visited = []

    if source in visited:
        return

    visited.append(source)

    for n in graph.incident_edges(source):
        dfs_explore_rec(graph, n, visited)

    return visited


def dfs_explore_it(graph, source):
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


if __name__ == "__main__":
    g = Graph()

    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('E')
    g.add_vertex('F')
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

    print(dfs_explore_rec(g, 'A'))
    print(dfs_explore_rec(g, 'F'))

    print(dfs_explore_it(g, 'A'))
    print(dfs_explore_it(g, 'F'))
