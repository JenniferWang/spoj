def eggDrop(n, k):
	"""
	http://www.geeksforgeeks.org/dynamic-programming-set-11-egg-dropping-puzzle/
	n : number of eggs
	k : number of floors
	"""
	dp = [[float('inf') for y in range(k + 1)] for x in range(n)]
	for y in range(k + 1):
		dp[0][y] = y
	for x in range(n):
		dp[x][0] = 0
		dp[x][1] = 1

	for x in range(1, n):
		for y in range(1, k + 1):
			for z in range(1, y):
				res = 1 + max(dp[x - 1][z - 1], dp[x][y - z])
				if res < dp[x][y]:
					dp[x][y] = res
	return dp[n - 1][k]

print eggDrop(2, 36) == 8 # = 8
print eggDrop(2, 10) == 4