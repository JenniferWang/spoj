import sys
def knapsack(weights, values, capacity):
  pre = [0 for j in range(capacity + 1)]
  for index, weight in enumerate(weights):
    curr = [0]
    for c in range(1, capacity + 1):
      curr_max_val = pre[c]
      if c - weight > -1:
        curr_max_val = max(curr_max_val, pre[c - weight] + values[index])
      curr.append(curr_max_val)
    pre = curr
  return pre[-1]

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