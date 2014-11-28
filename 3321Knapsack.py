import sys
def knapsack(weights, values, capacity):
  m = len(weights) + 1
  n = capacity + 1

  dp = [[0 for y in xrange(n)] for x in xrange(m)]

  for i in xrange(1, m):
    for j in xrange(1, n): # Here the boundary condition has already been merged to the initialization of dp
      if weights[i - 1] <= j:  # put item i
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
      else:
        dp[i][j] = dp[i - 1][j]
  return dp[m - 1][n - 1]

def main():
  g=sys.stdin
  #g = open("KNAPSACK", "r") 
  s=g.read().splitlines()
  while '' in s: s.remove('')
  while '\n' in s: s.remove('\n')
  
  firstLine = s[0].split()
  capacity = int(firstLine[0])
  num = int(firstLine[1])

  weights = []
  values = []
  for i in range(1, len(s)):
    line = s[i].split()
    weights.append(int(line[0]))
    values.append(int(line[1]))
  print knapsack(weights, values, capacity)

if __name__=='__main__':
  main()