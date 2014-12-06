# Practice disjoint set
# http://www.spoj.com/problems/FOXLINGS/
class DisjointSet():
  def __init__(self, n):
    self.root = {}
    self.num = n # number of disjoint sets
    self.sz = {}

  def findRoot(self, val):
    if val not in self.root:
      self.root[val] = val
      self.sz[val] = 1
      return val

    while val != self.root[val]:
      self.root[val] = self.root[self.root[val]]
      val = self.root[val]
    return val

  def union(self, val1, val2):
    val1 = self.findRoot(val1)
    val2 = self.findRoot(val2)
    if val1 == val2:
      return
    if self.sz[val1] > self.sz[val2]:
      self.root[val2] = val1
      self.sz[val1] += self.sz[val2]
    else:
      self.root[val1] = val2
      self.sz[val2] += self.sz[val1]
    self.num -= 1

  def getNumOfDisjointSet(self):
    return self.num

def main():
  #g = sys.stdin
  g = open("FOXLINGS", "r") 
  s = g.readline()
  l1 = s.split( )
  num_nodes = int(l1[0])
  num_edges = int(l1[1])

  djSet = DisjointSet(num_nodes)

  # for line in g:
  #   edge = line.split()
  #   djSet.union(int(edge[0]) - 1, int(edge[1]) - 1)

  for _ in range(num_edges):
    line = g.readline()
    edge = line.split()
    djSet.union(int(edge[0]) - 1, int(edge[1]) - 1)

  print(djSet.getNumOfDisjointSet())

if __name__ == '__main__':
  main()


  
