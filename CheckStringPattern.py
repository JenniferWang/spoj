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
	"""
	I wouldn’t like having this question in an interview, 
	because I think this is a kind of “Uh huh! This is the trick!” question.
	
	Let’s take "zzxzzxzzx" as an example. 
	If the string can be written as nS, where n > 1, then its suffix is (n-1) * S.
 	
 	ZZXZZXZZX 
     ZZXZZX
	
	Now, we need to add the S to the end somehow. We don’t know the actual length, 
	so we add the whole original string instead, i.e. we take the original string twice.

	ZZXZZXZZXZZXZZXZZX

	Now, to get |S|, simply search for the position of the original string starting at 
	the second character (string search is a common function in all languages). 
	If it returns |original string|, it means it found the concatenated string and we 
	simply return False. Otherwise, |S| != |original string|, therefore original string = n*S 
	and we return True.
	"""
	newString = string * 2
	if newString.find(string, 1, len(newString)) == len(string):
			return False
	return True

print checkIsMultiplication("abab")
print checkIsMultiplication("abcdabcd")
print checkIsMultiplication("abcabcabc")
print checkIsMultiplication("zzxzzxzzx")
print checkIsMultiplication("abac")
print checkIsMultiplication("abcdabbd")
print checkIsMultiplication("abcabcefg")
print checkIsMultiplication("zzxzzyzzx")