def findDP(L):
	n = len(L)
	dp = [None for x in range(n)]
	dp[0] = 1
	path = [[] for x in range(n)]
	path[0] = [L[0]]

	for i in range(1, n):
		step = 0
		dp[i] = 1
		path[i] = [L[i]]
		for j in range(i - 1, -1, -1):
			if L[j] < L[i]:
				step += 1
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



#L = [3, 2, 1, 4, 10, 6, 8, 7, 9]
#L = [10, 22, 9, 33, 21, 50, 41, 60, 80]
L = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
#L = [0, 8, 4, 12, 2]
print findDP(L)
print find(L)