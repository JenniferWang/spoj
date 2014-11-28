import sys
def findSeq(str1, str2):
  m = len(str1)
  n = len(str2)
  if n == 0 or m == 0:
    print 0

  dp = [[0 for y in range(n)] for x in range(m)]
  for j in range(1, n + 1):
    if str1[0] in str2[: j]:
      dp[0][j - 1] = 1

  for i in range(1, m + 1):
    if str2[0] in str1[: i]:
      dp[i - 1][0] = 1

  for i in range(1, m):
    for j in range(1, n):
      if str1[i] == str2[j]:
        dp[i][j] = 1 + dp[i - 1][j - 1]
      else:
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

  print dp[m - 1][n - 1]

def main():
  #g=sys.stdin
  g = open("LCS0", "r") 
  s=g.read().splitlines()
  while '' in s: s.remove('')
  while '\n' in s: s.remove('\n')
  str1 = s[0]
  str2 = s[1]
  findSeq(str1, str2)

if __name__=='__main__':
  main()
