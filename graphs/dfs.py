graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

graph2 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B', 'E', 'F'],
    'E': ['B', 'C', 'D', 'F'],
    'F': ['D', 'E']
}

graph3 = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}


def dfs_iterative(input_graph, start):
    """ Depth first search result """
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)    # faster search
            result.append(node)  # maintains order
            for adj_node in reversed(input_graph[node]):
                stack.append(adj_node)


    return result

def dfs_recursive(input_graph, start, visited=None, result=None):
    if not visited:
        visited = set([start])
    if not result:
        result = [start]

    for adj_node in input_graph[start]:
        if adj_node not in visited:
            visited.add(adj_node)
            result.append(adj_node)
            dfs_recursive(input_graph, adj_node, visited, result)


    return result




print dfs_iterative(graph, 'A')
print dfs_iterative(graph, 'C')
print dfs_iterative(graph3, 2)

print dfs_recursive(graph, 'A')
print dfs_recursive(graph, 'C')
print dfs_recursive(graph3, 2)
