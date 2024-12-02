def bfs(graph, start, path = []):
  queue = [start]
  while queue:
    vertex = queue.pop(0)
    if vertex not in path:
      path = path + [vertex]
      queue = queue + graph[vertex]
  return path


if __name__ == '__main__':

  graph = {'A':['B','C','D'],
           'B':['E'],
           'C':['F','G'],
           'D':['H'],
           'E':['I'],
           'F':['J'],
           'G':[],
           'H':[],
           'I':[],
           'J':[]}  
  
print('bfs: ', bfs(graph, 'A'))
