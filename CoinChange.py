def change(valueList, summation):
  # http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/
  dp = {}
  # assume all values are positive
  for i in range(len(valueList)):
    dp[(i, 0)] = 1
  for j in range(summation + 1):
    if j % valueList[0] == 0:
      dp[(0, j)] = 1
      continue
    dp[(0, j)] = 0
  dp[(0,0)] = 1

  for i in range(1, len(valueList)):
    for sm in range(summation + 1):
      k = 1
      dp[(i, sm)] = dp[(i - 1, sm)]
      while sm - k * valueList[i] >= 0: # Attention, every coin can be taken infinite times
        dp[(i, sm)] += dp[(i - 1, sm - k * valueList[i])]
        k += 1
  return dp[(len(valueList) - 1, summation)]

print change([2, 5, 3, 6], 10)