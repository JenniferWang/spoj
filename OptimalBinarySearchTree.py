def optCost(freqs):
  """
  http://www.geeksforgeeks.org/dynamic-programming-set-24-optimal-binary-search-tree/
  cost definitin is calcuated according to 
  http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1245
  """
  n = len(freqs)
  cost = [[None for y in xrange(n)] for x in xrange(n)]
  for start in xrange(n):
    cost[start][start] = 0

  for length in xrange(2, n + 1):
    for start in xrange(n - length + 1):
      summation = sum(freqs[start: start + length])
      cost[start][start + length - 1] = min(
        summation - freqs[start] + cost[start + 1][start + length - 1],
        summation - freqs[start + length - 1] + cost[start][start + length - 2]
      ) 
      
      for k in xrange(start + 1, start + length - 1):
        cost[start][start + length - 1] = min(
          cost[start][start + length - 1],
          cost[start][k - 1] + cost[k + 1][start + length - 1] + summation - freqs[k]
        )

  return cost[0][n - 1]


def main():
  #g=sys.stdin
  g = open("OptimalBST", "r") 
  s=g.read().splitlines()
  while '' in s: s.remove('')
  while '\n' in s: s.remove('\n')
  
  for i in range(len(s)):
    line = s[i].split()
    freqs = line[1:]
    freqs = map(int, freqs) # Attention
    print optCost(freqs)

if __name__=='__main__':
  main()