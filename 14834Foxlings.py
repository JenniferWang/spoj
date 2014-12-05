# Practice disjoint set
# http://www.spoj.com/problems/FOXLINGS/
class DisjointSet():
  def __init__(self, n):
    self.root = [x for x in xrange(n)]
    self.num = n # number of disjoint sets
    self.sz = [1 for x in xrange(n)]

  def findRoot(self, val):
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

  def find(self, val1, val2):
    val1 = self.findRoot(val1)
    val2 = self.findRoot(val2)
    return val1 == val2

  def getNumOfDisjointSet(self):
    return self.num

def main():
  #g=sys.stdin
  g = open("FOXLINGS", "r") 
  s=g.read().splitlines()
  while '' in s: s.remove('')
  while '\n' in s: s.remove('\n')

  l1 = s[0].split( )
  num_nodes = int(l1[0])
  num_edges = int(l1[1])
  djSet = DisjointSet(num_nodes)
  for edge in xrange(1, num_edges + 1):
    l = s[edge].split( )
    djSet.union(int(l[0]) - 1, int(l[1]) - 1)

  print djSet.getNumOfDisjointSet()
   
if __name__ == '__main__':
  main()


  
