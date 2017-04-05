"""
When a graph is not connected, the next goal we may have is to identify all of
the connected components of an undirected graph, or the strongly connected components of a directed graph.
We begin by discussing the undirected case. If an initial call to DFS fails to reach all vertices of a graph,
we can restart a new call to DFS at one of those unvisited vertices.

Although the DFS complete function makes multiple calls to the original DFS function,
the total time spent by a call to DFS complete is O(n + m).
"""

from algorithms.graphs.dfs.dfs import _DFS_map


def dfs_complete(graph):
    """
    Perform DFS for entire graph and return forest as a dictionary.
    Result maps each vertex v to the edge that was used to discover it.
    (Vertices that are roots of a DFS tree are mapped to None.)
    """

    forest = {}

    for u in graph.vertices():
        if u not in forest:

            # u will be the root of the tree
            forest[u] = None

            _DFS_map(graph, u, forest)

    return forest
