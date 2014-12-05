# Practice disjoint set
class DisjointSet():
	def __init__(self, n):
		self.data = [x for x in xrange(n)]
		self.id = [x for x in xrange(n)]
		self.num = n # number of disjoint sets
		self.sz = [1 for x in xrange(n)]
		self.n = n
	def findRoot(self, val):
		if val not in range(self.n):
			print 'val1 or val2 out of range'
			return
		while val != self.id[val]:
			self.id[val] = self.id[self.id[val]]
			val = self.id[val]
		return val
	def union(self, val1, val2):
		if val1 not in range(self.n) or val2 not in range(self.n):
			print 'val1 or val2 out of range'
			return
		val1 = self.findRoot(val1)
		val2 = self.findRoot(val2)
		if val1 == val2:
			return
		if self.sz[val1] > self.sz[val2]:
			self.id[val2] = val1
			self.sz[val1] += self.sz[val2]
		else:
			self.id[val1] = val2
			self.sz[val2] += self.sz[val1]
		self.num -= 1

	def find(self, val1, val2):
		val1 = self.findRoot(val1)
		val2 = self.findRoot(val2)
		return val1 == val2

test = 	DisjointSet(10)
print test.id
test.union(3, 4)
print '3 - 4'
print test.id
print test.sz

test.union(4,9)
print '4 - 9'
print test.id
print test.sz

test.union(2, 3)
print '2 - 3'
print test.id
print test.sz
print test.num
test.union(2,2)
print test.id
print test.find(4, 9)
	
