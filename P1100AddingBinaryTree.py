#https://vijos.org/p/1100
class AddingBinaryTree():
  def __init__(self, values, n):
    self.values = values
    self.n = n
    self.preorderResult = []

  def addingBinaryTree(self):
    n = self.n
    scores = [[None for y in range(n)] for x in range(n)]
    choices = [[None for y in range(n)] for x in range(n)]

    for m in range(n):
      scores[m][m] = self.values[m]
      choices[m][m] = m

    for length in range(2, n + 1):
      for start in range(n - length + 1):
        if not scores[start][start + length - 1]:
          scores[start][start + length - 1] = float('-inf')
        for k in range(start, start + length):
          if k == start:
            curr_score = scores[k + 1][start + length - 1] + self.values[k]
          elif k == start + length - 1:
            curr_score = scores[start][k - 1] + self.values[k]
          else:
            curr_score = scores[start][k - 1] * scores[k + 1][start + length - 1] + self.values[k]
          if curr_score > scores[start][start + length - 1]:
            choices[start][start + length - 1] = k
            scores[start][start + length - 1] = curr_score

    self.choices = choices
    self.scores = scores[0][n - 1]
    

  def preorderPrint(self, n, m):
    self.preorderResult.append(self.choices[n][m] + 1)
    if self.choices[n][m] - 1 >= n :
      self.preorderPrint(n, self.choices[n][m] - 1)
    if self.choices[n][m] + 1 <= m :
      self.preorderPrint(self.choices[n][m] + 1, m)

def main():
  #g=sys.stdin
  g = open("P1100", "r") 
  s=g.read().splitlines()
  while '' in s: s.remove('')
  while '\n' in s: s.remove('\n')
  
  numNodes = int(s[0])
  values = map(int,s[1].split())

  tree = AddingBinaryTree(values, numNodes)
  tree.addingBinaryTree()
  tree.preorderPrint(0, numNodes - 1)
  print tree.scores
  for item in tree.preorderResult:
    print item,

if __name__=='__main__':
  main()