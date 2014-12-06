# Given an input string S write a function which returns true if it 
# satisfies S = nT. Basically you have to find if a given string can 
# be represented from a substring by iterating it "n" times. n >= 2

# Function should return true if
# 1) S = "abab"
# 2) S = "abcdabcd"
# 3) S = "abcabcabc"
# 4) S = "zzxzzxzzx"
# Function should return false if
# 1) S = "abac"
# 2) S = "abcdabbd"
# 3) S = "abcabcefg"
# 4) S = "zzxzzyzzx"

def checkIsMultiplication(string):
	for length in xrange(1, len(string)):
		newString = string + string[:length]
		if newString.find(string, 1, len(newString)) > 0:
			return True
	return False

# print checkIsMultiplication("abab")
# print checkIsMultiplication("abcdabcd")
# print checkIsMultiplication("abcabcabc")
# print checkIsMultiplication("zzxzzxzzx")
print checkIsMultiplication("abac")
# print checkIsMultiplication("abcdabbd")
# print checkIsMultiplication("abcabcefg")
# print checkIsMultiplication("zzxzzyzzx")