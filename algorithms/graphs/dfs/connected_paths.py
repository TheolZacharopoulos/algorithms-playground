"""
We can use the basic DFS function as a tool to identify the (directed) path leading from vertex source to dest,
if dest is reachable from source. This path can easily be reconstructed from the information that was recorded in
the discovery dictionary during the traversal.

To reconstruct the path, we begin at the end of the path (dest),
examining the discovery dictionary to determine what edge was used to reach vertex dest,
and then what the other endpoint of that edge is.
We add that vertex to a list, and then repeat the process to determine what edge was used to discover it.
Once we have traced the path all the way back to the starting vertex source,
we can reverse the list so that it is properly oriented from source to dest, and return it to the caller.

This process takes time proportional to the length of the path,
and therefore it runs in O(n) time (in addition to the time originally spent calling DFS).
"""


def _construct_path(source, dest, discovered):
    """
    Return a list of vertices comprising the directed path from u to v,
    or an empty list if v is not reachable from u.
    discovered is a dictionary resulting from a previous call to DFS started at u.
    """
    path = []  # empty path by default

    if dest in discovered:
        # we build list from dest to source and then reverse it at the end
        path.append(dest)

        walk = dest

        while walk is not source:
            e = discovered[walk]  # find edge leading to walk
            parent = e.opposite(walk)
            path.append(parent)
            walk = parent

        path.reverse()  # reorient path from u to v

    return path


def construct_path(source, dest):
    return _construct_path(source, dest, {source: None})
