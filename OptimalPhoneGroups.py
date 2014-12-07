# You are given a String number containing the digits of a phone number
# (the number of digits, n, can be any positive integer) . To help you 
# memorize the number, you want to divide it into groups of contiguous digits.
# Each group must contain exactly 2 or 3 digits. There are three kinds of groups:
# Excellent: A group that contains only the same digits. For example, 000 or 77.
# Good: A group of 3 digits, 2 of which are the same. For example, 030, 229 or 166.
# Usual: A group in which all the digits are distinct. For example, 123 or 90.
# The quality of a group assignment is defined as 2*(number of excellent groups)+ 
# (number of good groups)
# Divide the number into groups such that the quality is maximized.
# Design an efficient algorithm to return the solution that maximizes the quality.
class OptimalPhoneGroup():

	def __init__(self, string):
		self.s = string

	def isExcellent(self, substring):
		return substring == substring[0] * len(substring)

	def isGood(self, substring):
		return len(substring) == 3 and len(set(substring)) < 3

	def subStringValue(self, substring):
		if self.isExcellent(substring):
			return 2
		if self.isGood(substring):
			return 1
		return 0

	def findOptimalGroup(self):
		if len(self.s) == 1:
			return 'no solution'

		value = [0, -len(self.s) * 2]
		partition = [None, None]

		for index in range(1, len(self.s)):
			possible_choice = [self.s[index - 1: index + 1]]
			if index >= 2:
				possible_choice.append(self.s[index - 2: index + 1])
			cur_max = -1
			cur_argmax = None
			for substring in possible_choice:
				if cur_max < value[index - len(substring) + 1] + self.subStringValue(substring):
					cur_max = value[index - len(substring) + 1] + self.subStringValue(substring)
					cur_argmax = index - len(substring) + 1
			partition.append(cur_argmax)
			value.append(cur_max)

		cur_ind = len(self.s)
		path = []
		while cur_ind and cur_ind >= 0:
			path.append(self.s[partition[cur_ind]: cur_ind])
			cur_ind = partition[cur_ind]
		return path[::-1], value[-1]

print OptimalPhoneGroup('77').findOptimalGroup()
print OptimalPhoneGroup('7701').findOptimalGroup()
print OptimalPhoneGroup('000').findOptimalGroup()
print OptimalPhoneGroup('011000').findOptimalGroup()
print OptimalPhoneGroup('000000').findOptimalGroup()
print OptimalPhoneGroup('00000').findOptimalGroup()
print OptimalPhoneGroup('000000000000000000000000000000').findOptimalGroup()
print OptimalPhoneGroup('0000000000000000000000000000000').findOptimalGroup()
print OptimalPhoneGroup('1').findOptimalGroup()