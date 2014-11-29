def optCost(freqs):
  n = len(freqs)
  max_freq = max(freqs)
  cost = [[None for y in range(n)]for x in range(n)]
  for x in range(n):
    cost[x][x] = 0

  for length in range(2, n + 1):
    for x in range(n - length + 1):
      summation = sum(freqs[x: x + length])
      cost[x][x + length - 1] = min(
        summation - freqs[x] + cost[x + 1][x + length - 1],
        summation - freqs[x + length - 1] + cost[x][x + length - 2]
      ) 
      
      for k in range(x + 1, x + length - 1):
        cost[x][x + length - 1] = min(
          cost[x][x + length - 1],
          cost[x][k - 1] + cost[k + 1][x + length - 1] + summation - freqs[k]
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
    freqs = [int(x) for x in freqs]
    print optCost(freqs)

if __name__=='__main__':
  main()