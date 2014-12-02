#https://vijos.org/p/1100
def addingBinaryTree(values, n):
  scores = [[1 for y in range(n)] for x in range(n)]
  choices = [[None for y in range(n)] for x in range(n)]

  for m in range(n):
    scores[m][m] = values[m]
    choices[m][m] = m

  for length in range(2, n + 1):
    for start in range(n - length + 1):
      for k in range(start, start + length):
        if k == start:
          curr_score = scores[k + 1][start + length - 1] + values[k]
        elif k == start + length - 1:
          curr_score = scores[start][k - 1] + values[k]
        else:
          curr_score = scores[start][k - 1] * scores[k + 1][start + length - 1] + values[k]
        if curr_score > scores[start][start + length - 1]:
          choices[start][start + length - 1] = k
          scores[start][start + length - 1] = curr_score

  print scores[0][n - 1]
  return choices

def preorderPrint(n, m, preorderResult, values, choices):
  preorderResult.append(choices[n][m] + 1)
  if choices[n][m] - 1 >= n :
    preorderPrint(n, choices[n][m] - 1, preorderResult, values, choices)
  if choices[n][m] + 1 <= m :
    preorderPrint(choices[n][m] + 1, m, preorderResult, values, choices)

def main():
  #g=sys.stdin
  g = open("P1100", "r") 
  s=g.read().splitlines()
  while '' in s: s.remove('')
  while '\n' in s: s.remove('\n')
  
  numNodes = int(s[0])
  values = map(int,s[1].split())

  choices = addingBinaryTree(values, numNodes)
  preorderResult = []
  preorderPrint(0, numNodes - 1, preorderResult, values, choices)
  print ' '.join([str(item) for item in preorderResult])

if __name__=='__main__':
  main()