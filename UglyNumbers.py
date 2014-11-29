def findUgly(n):
	"""
	find the nth ugly number
	"""
	i2, i3, i5 = 0, 0, 0
	ugList = [1]
	for i in range(n - 1):
		candidates = [ugList[i2] * 2, ugList[i3] * 3, ugList[i5] * 5]
		curr = candidates.index(min(candidates)) # Attention .index method
		if curr == 0:
			ugList.append(ugList[i2] * 2) # Attention: first append, then i2 ++
			i2 += 1
			continue
		if curr == 1:
			ugList.append(ugList[i3] * 3)
			i3 += 1
			continue
		if curr == 2:
			ugList.append(ugList[i5] * 5)
			i5 += 1
			continue

	return ugList[n - 1]
print findUgly(150)