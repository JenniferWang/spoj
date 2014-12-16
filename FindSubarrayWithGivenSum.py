def findSubarray(arr, summ):
	"""
	http://www.geeksforgeeks.org/find-subarray-with-given-sum/
	Note the entries are nonnegative
	"""
	curr = 0
	left = 0

	for right in xrange(len(arr)):
		if arr[right] == summ:
			return arr[right: right + 1]

		curr += arr[right]
		if curr == summ:
			return arr[left: right + 1]	

		while left <= right and curr > summ:
			curr -= arr[left]
			left += 1
			if curr == summ:
				return arr[left: right + 1]
			
	return None	

# print findSubarray([1], 1)
# print findSubarray([1, 2], 2)
# print findSubarray([1, 3, 2], 10)
# print findSubarray([1, 4, 20, 3, 10, 5], 33)
# print findSubarray([1, 4, 0, 0, 3, 10, 5], 7)

def findSubarrayNegIncluded(arr, summ):
	dic = {}
	curr = 0
	for right in xrange(len(arr)):
		if arr[right] == summ:
			return arr[right]
		curr += arr[right]
		dic[curr] = right + 1
		if curr - summ in dic:
			return arr[dic[curr - summ] : right + 1]
	return None

# print findSubarrayNegIncluded([1], 1)
# print findSubarrayNegIncluded([1, 2], 2)
# print findSubarrayNegIncluded([1, 3, 2], 10)
# print findSubarrayNegIncluded([1, 4, 20, 3, 10, 5], 33)
# print findSubarrayNegIncluded([1, 4, 0, 0, 3, 10, 5], 7)
print findSubarrayNegIncluded([-1, 4, 0, 0, -3, 10, 5], 1)


