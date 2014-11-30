def minJumps(L):
	n = len(L)
	if n == 0:
		return 0

	ends = [0] # if the first node is the end node, don't need to move any more
	paths = [[L[0]]]
	for end in xrange(1, n):
		curr_min = float('inf')
		for stop in xrange(end):
			if L[stop] >= end - stop:
				jump = 1 + ends[stop]
				if curr_min > jump:
					curr_min = jump
					path = paths[stop] + [L[end]]
		ends.append(curr_min)
		paths.append(path)
	print paths[-1]
	return ends[-1]

print minJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9])