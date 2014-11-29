def partition(arr, summ):
	"""
	http://www.geeksforgeeks.org/dynamic-programming-set-18-partition-problem/
	"""
	n = len(arr)
	pre = [False for x in range(summ + 1)]
	pre[0] = True

	for i in range(0, n):
		print pre
		curr = []
		for sm in range(summ, -1, -1):
			if sm - arr[i] >= 0:
				curr = [pre[sm - arr[i]] or pre[sm]] + curr
				continue
			curr = [pre[sm]] + curr # Attention, reversed order !
		pre = curr
	return pre[-1]
	
def partition_main(arr):
	summ = sum(arr)
	if summ % 2 == 1:
		return False
	return partition(arr, summ / 2)

print partition_main([3, 1, 1, 2, 2, 1]) == True

