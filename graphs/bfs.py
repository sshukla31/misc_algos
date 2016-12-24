graph1 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': []
}
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

graph3 = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}


class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.insert(0, value)

    def dequeue(self):
        if self.queue:
            return self.queue.pop()
        else:
            print "Queue is empty"
            return None

    def is_empty(self):
        return False if self.queue else True


def bfs_iterative(input_graph, start):
    queue = Queue()
    queue.enqueue(start)
    visited = set()
    result = []

    while not queue.is_empty():
        node = queue.dequeue()
        if node not in visited:
            visited.add(node)
            result.append(node)
            adj_nodes = input_graph.get(node, [])
            for adj_node in adj_nodes:
                queue.enqueue(adj_node)

    return result


print bfs_iterative(graph3, 2)
print bfs_iterative(graph, 'A')