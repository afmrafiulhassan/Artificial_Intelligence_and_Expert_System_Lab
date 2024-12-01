def dfs(graph, start):
    path = []
    stack = [start]
    while stack:
        v = stack.pop(0)
        if v not in path:
            path.append(v)
            stack = graph.get(v, []) + stack
    return path

if __name__ == '__main__':
    graph = {'A': ['B', 'C', 'D'],
             'B': ['E'],
             'C': ['F', 'G'],
             'D': ['H'],
             'E': ['I'],
             'F': ['J'],
             'G': [],
             'H': [],
             'I': [],
             'J': []}
    print('dfs: ', dfs(graph, 'A'))
