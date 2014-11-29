class Treenode():
	def __init__(self, value):
		self.value = value
		self.right = None
		self.left = None

cache = {}
def findLIS(root):
	"""
	Only need to compute the size of the subsets
	http://www.geeksforgeeks.org/largest-independent-set-problem/
	"""
	global cache
	if root == None:
		return 0
	if (not root.left) and (not root.right):
		return 1
	if root in cache:
		return cache[root]

	candidates = [0, 0]
	if root.left:
		candidates[0] += findLIS(root.left)
		candidates[1] += findLIS(root.left.left)
		candidates[1] += findLIS(root.left.right)
	if root.right:
		candidates[0] += findLIS(root.right)
		candidates[1] += findLIS(root.right.left)
		candidates[1] += findLIS(root.right.right)
	if candidates[1] > 0:
		candidates[1] += 1

	cache[root] = max(candidates)
 	return cache[root]

node1 = Treenode(10)
node2 = Treenode(20)
node3 = Treenode(30)
node1.left = node2
node1.right = node3
node4 = Treenode(40)
node5 = Treenode(50)
node6 = Treenode(60)
node2.left = node4
node2.right = node5
node3.right = node6
node7 = Treenode(70)
node8 = Treenode(80)
node5.left = node7
node5.right = node8
print findLIS(node1)

