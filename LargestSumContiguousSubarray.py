def maxSubarraySum(L):
	"""
	Given an 1-D array, return the maximum sum of contiguous subarray
	http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
	recursion relation is a little tricky
	"""
	n = len(L)
	if n == 0:
		return None
	subarraysum = [L[0]] # Just update the latest is ok, don't need to store
	max_sum = subarraysum[0]
	for end in xrange(1, n):
		subarraysum.append(max(subarraysum[- 1] + L[end], L[end]))
		max_sum = max(max_sum, subarraysum[-1])
	return max_sum

print maxSubarraySum([-2, -3, 4, -1, -2, 1, 5, -3])

