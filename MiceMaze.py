# template
# f output file
# g input file
import sys

# def floyd(num_cells, edgelist, exit):
#     matrixTable = [[float('inf') for y in range(num_cells)] for x in range(num_cells)]
#     for edge in edgelist:
#       matrixTable[edge[0] - 1][edge[1] - 1] = edge[2]
#     matrixTable[exit -1][exit - 1] = 0
#     n = len(matrixTable)
#     for k in range(n):
#       for i in range(n):
#         for j in range(n):
#           matrixTable[i][j] = min(matrixTable[i][j], matrixTable[i][k] + matrixTable[k][j])
#     return matrixTable

class DirectedGraph( ):

  def __init__(self, edgeDic, src):
    self.edgeDic = edgeDic
    self.num_cells = len(edgeDic)
    self.src = src
    self.dist = {x: float('inf') for x in edgeDic}
    self.dist[self.src] = 0

  def dijkstra(self):
    if self.src not in self.edgeDic:
      raise TypeError('root not in graph')
    queue = []
    visited = []  

    for node in self.edgeDic:
      queue.append(node)

    distance = {x : self.dist[x] for x in self.edgeDic}
    while queue:
      curr = min(distance, key = distance.get) # Attention
      queue.remove(curr)
      visited.append(curr)
      del distance[curr] # Attention

      for neighbor in self.edgeDic[curr]:
        if neighbor not in visited: # Attention
          self.dist[neighbor] = min(self.dist[neighbor], \
            self.dist[curr] + self.edgeDic[curr][neighbor])
          distance[neighbor] = self.dist[neighbor]
    return self.dist

def main():
  #g=sys.stdin
  g = open("micemaze", "r") 
  s=g.read().splitlines()
  while '' in s: s.remove('')
  while '\n' in s: s.remove('\n')
  num_cells = int(s[0])
  exit_cell = s[1].strip() 
  time_start = int(s[2])
  num_edges = int(s[3])
  ## test case###
  edgeDic = {str(x + 1):{} for x in range(num_cells) }
  for i in range(num_edges):
    edge = s[i + 4].split()
    edgeDic[edge[1]][edge[0]] = float(edge[2]) # Reverse the edges as we are actually
  maze = DirectedGraph(edgeDic, exit_cell)     # finding the shortest path to the destination

  ### test case ###
  # edgeDic = {'s': {'a': 2, 'b': 1},
  #         'a': {'s': 3, 'b': 4, 'c':8},
  #         'b': {'s': 4, 'a': 2, 'd': 2},
  #         'c': {'a': 2, 'd': 7, 't': 4},
  #         'd': {'b': 1, 'c': 11, 't': 5},
  #         't': {'c': 3, 'd': 5}}
  # maze = DirectedGraph(edgeDic, 's')

  distDict = maze.dijkstra()
  count = 0
  for key in distDict:
    if distDict[key] <= time_start:
      count += 1
  print count

if __name__=='__main__':
  main()
