# This is just an implementation of Huffman encoding
from pprint import pprint
from heapq import heappush, heappop, heapify
class Haffman():
	def __init__(self, wordDic):
		self.wordDic = wordDic
		self.encodingRule = {}

	def encode(self):
		heap = [[freq, [sym, '']] for sym, freq in self.wordDic.items()] # Attention
		heapify(heap)

		while len(heap) > 1: # we assign '0', '1' on edges, not on nodes
			pprint(heap)
			print 
			left = heappop(heap)
			right = heappop(heap) # add to every current coding pari
			for pair in left[1:]:
				pair[1] = '0' + pair[1]
			for pair in right[1:]:
				pair[1] = '1' + pair[1]
			heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])

		print heap
		
	def decode(self, text):
		pass


test = Haffman({'a':1, 'b':1, 'c':2, 'd':3, 'e':5, 'g': 13, 'h':2})
test.encode()