import sys

cache ={}
def coinChange(n):
	global cache
	if n == 0:
		cache[0] = 0
		return 0
	if n in cache:
		return cache[n]
	cache[n] = max(n, coinChange(n/3) + coinChange(n/4) + coinChange(n/2))
	return cache[n]

def main():
  g=sys.stdin
  #g = open("COINS", "r") 
  s=g.read().splitlines()
  while '' in s: s.remove('')
  while '\n' in s: s.remove('\n')
  for num in s:
  	print coinChange(int(num))

if __name__=='__main__':
  main()