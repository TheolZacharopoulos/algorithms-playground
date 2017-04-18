from algorithms.graphs.SimpleGraph import Graph

"""
Search if a vertex (destination) is reachable from another (source),
using the depth first search.
"""


def dfs_rec(graph, source, dest, visited=None):
    if visited is None:
        visited = []

    if source in visited:
        return False

    if source == dest:
        return True

    visited.append(source)

    for n in graph.incident_edges(source):
        if dfs_rec(graph, n, dest, visited):
            return True
    return False


def dfs_it(graph, source, dest):
    stack = []
    visited = []

    stack.append(source)

    while stack:
        v = stack.pop()

        if v == dest:
            return True

        if v in visited:
            continue

        visited.append(v)

        for n in graph.incident_edges(v):
            stack.append(n)

    return False


def _DFS_map(g, u, discovered):
    """
    Perform DFS of the undiscovered portion of Graph g starting at Vertex u.
    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the DFS. (u should be "discovered" prior to the call.)
    Newly discovered vertices will be added to the dictionary as a result.
    """
    for e in g.incident_edges(u):  # for every outgoing edge from u
        v = e.opposite(u)
        if v not in discovered:  # v is an unvisited vertex
            discovered[v] = e  # e is the tree edge that discovered v
            _DFS_map(g, v, discovered)  # recursively explore from v


def DFS_map(g, u):
    return _DFS_map(g, u, {u : None})


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

    print(dfs_it(g, 'B', 'F'))
    print(dfs_rec(g, 'B', 'F'))

    print(dfs_it(g, 'A', 'J'))
    print(dfs_rec(g, 'A', 'J'))
