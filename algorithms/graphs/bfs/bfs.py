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
