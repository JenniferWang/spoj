class RadixSort():
	def __init__(self, data, b):
		"""
		assume all the data are integers, ranging from 0 to max_data
		"""
		self.data = data
		self.base = b

	def getMax(self):
		self.max_data = max(self.data)
		return self.max_data

	def countingSort(self, exp):
		self.sorted = self.data[:]
		count = [0 for x in xrange(self.base)]
		for d in self.sorted:
			count[(d / exp) % self.base] += 1

		for x in xrange(1, self.base):
			count[x] += count[x - 1]

		curr_data = [None for d in self.sorted]
		for d in self.sorted:
			remain = (d / exp) % self.base
			index = count[remain] - 1
			curr_data[index] = d
			count[remain] -= 1
			
		self.sorted = curr_data

	def radixSort(self):
		exp = 1
		max_data = self.getMax()
		while max_data / exp != 0:
			self.countingSort(exp)
			exp *= self.base
		return self.sorted

countingsort = RadixSort([3, 2, 1, 9, 8], 2)
print countingsort.radixSort()

