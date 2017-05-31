"""
Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
"""


# Use bfs
def connectivity(start, dest):
    visited = []
    queue = [start]

    while queue:
        v = queue.pop(0)

        if v == dest:
            return True

        if v in visited:
            continue

        visited.append(v)

        for u in v.adjacent():
            queue.append(u)
    return False
