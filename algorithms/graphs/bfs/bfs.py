def bfs(graph, source, dest):
    visited = []
    queue = [source]

    while queue:
        v = queue.pop(0)

        if v == dest:
            return True

        if v in visited:
            continue

        visited.append(v)

        for u in graph.incident_edges(v):
            queue.append(u)
    return False


def bfs_2(graph, source):
    visited = []
    queue = []

    queue.append(source)
    visited.append(source)

    while queue:
        v = queue.pop(0)

        for u in graph.incident_edges(v):
            if u not in visited:
                queue.append(u)
                visited.append(v)


def bfs_paths(graph, source):
    visited = []
    queue = []
    edge_to = {}

    queue.append(source)
    visited.append(source)

    while queue:
        v = queue.pop(0)

        for u in graph.incident_edges(v):
            if u not in visited:
                queue.append(u)
                visited.append(v)
                edge_to[u] = v
