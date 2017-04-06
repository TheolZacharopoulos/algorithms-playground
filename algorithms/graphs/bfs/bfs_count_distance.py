def bfs_distance(graph, source):
    dist = {}

    for u in graph.vertices():
        dist[u] = float('inf')

    dist[source] = 0

    queue = [source]

    while queue:
        v = queue.pop(0)

        for u in graph.incident_edges(v):
            if dist[u] == float('inf'):
                queue.append(u)
                dist[u] = dist[v] + 1

    return dist
