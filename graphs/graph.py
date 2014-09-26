graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C']
}


def find_path(graph, start, end, path=[]):
    """ Find path between 2 nodes with no duplicates """
    path = path + [start]
    if (start == end):
        return path
    else:
        if graph.get(start) is None:
            return None
        for node in graph[start]:
            if node not in path:
                new_path = find_path(graph=graph, start=node, end=end, path=path)
                if new_path is not None:
                    return new_path
        return None

def find_shortest_path(graph, start, end, path=[]):
    """ Find path between 2 nodes with no duplicates """
    path = path + [start]
    if (start == end):
        return path
    else:
        if graph.get(start) is None:
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                new_path = find_shortest_path(graph=graph, start=node, end=end, path=path)
                if new_path is not None:
                    if not shortest or len(new_path) < len(shortest):
                        shortest = new_path

        return shortest

print find_path(graph=graph, start='A', end='D')
print find_shortest_path(graph=graph, start='A', end='D')
