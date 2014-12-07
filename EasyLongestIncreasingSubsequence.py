def findDP(L):
  n = len(L)
  dp = [1 for x in range(n)]
  path = [[] for x in range(n)]
  path[0] = [L[0]]

  for i in range(1, n):
    path[i] = [L[i]]
    for j in range(i - 1, -1, -1):
      if L[j] < L[i]:
        dp[i] = max(dp[i], dp[j] + 1)
        if dp[i] == dp[j] + 1:
          path[i] = path[j] + [L[i]]

  print path[-1]
  return dp[-1]

def find(L):
  """
  Good explanation: 
  http://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
  """
  n = len(L)
  if n < 1:
    return 0
  currentList = [L[0]]
  for i in range(1, n):
    if L[i] > currentList[-1]:
      currentList.append(L[i])
      continue
    for j in range(len(currentList) - 1, -1, -1):
      if L[i] < currentList[j] and L[i] > currentList[j - 1]:
        currentList[j] = L[i]
        break
  return len(currentList)

def findMaxSum(L):
  """
  http://www.geeksforgeeks.org/dynamic-programming-set-14-maximum-sum-increasing-subsequence/
  """
  n = len(L)
  dp = [L[i] for i in range(n)]
  for i in range(1, n):
    for j in range(i - 1, -1 , -1):
      if L[j] < L[i]:
        dp[i] = max(dp[j] + L[i], dp[i])

  return max(dp)

def findBitonic(L):
  """
  http://www.geeksforgeeks.org/dynamic-programming-set-15-longest-bitonic-subsequence/
  """
  n = len(L)
  dpi = [1 for x in range(n + 1)]
  dpi[0] = 0
  dpd = [1 for y in range(n + 1)]
  dpd[-1] = 0
  for i in range(1, n + 1):
    for k in range(i - 1, 0, -1):
      if L[k - 1] < L[i - 1]:
        dpi[i] = max(dpi[k] + 1, dpi[i])

  for j in range(n - 1, -1, -1): # Attention index
    for k in range(j + 1, n):
      if L[k] < L[j]:
        dpd[j] = max(dpd[k] + 1, dpd[j])
      
  max_length = 0
  for m in range(n + 1):
    max_length = max(max_length, dpi[m] + dpd[m])
  return max_length

#L = [3, 2, 1, 4, 10, 6, 8, 7, 9]
#L = [10, 22, 9, 33, 21, 50, 41, 60, 80]
#L = [1, 101, 2, 3, 100, 4, 5]
L = [3, 4, 5, 10]
L = [10, 5, 4, 3]
#L = [10, 5, 4, 3]
L = [1, 11, 2, 10, 4, 5, 2, 1] # findBitonic = 6
L = [12, 11, 40, 5, 3, 1] # findBitonic = 5
L = [80, 60, 30, 40, 20, 10] # findBitonic = 5
L = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15] #findBitonic = 7
#print findMaxSum(L)
print find(L)
print findBitonic(L)
