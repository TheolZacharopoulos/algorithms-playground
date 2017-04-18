def degree(g, v):
    return len(g.get_edges(v))


def max_degree(g):
    max_degree = 0
    for v in g.vertices():
        max_degree = max(max_degree, g.degree(v))
    return max_degree


def number_of_self_loops(g):
    count = 0

    for v in g.vertices():
        for u in g.get_edges(v):
            if v == u:
                count += 1
    return count
