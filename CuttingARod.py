def cutRod(prices, n):
	v = [0] + [prices[x] for x in range(n)]
	for i in range(1, n + 1):
		for j in range(1, i):
			v[i] = max(v[i], v[i - j] + prices[j - 1])
	return v[n]

print cutRod([1, 5, 8, 9, 10, 17, 17, 20], 8)