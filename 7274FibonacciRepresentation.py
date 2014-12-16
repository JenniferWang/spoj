# http://www.spoj.com/problems/FIBOREP/
# Constraints: 
# T <= 1000  No of test cases
# 1 <= N <= 100000000 (10^8) 
# Fibs grows exponentially thus we can save the fibs
class FibonacciRep():
  def __init__(self):
    self.fibs = [1, 2]
    self.maxN = 10**8

  def calulateFib(self):
    while self.fibs[-2] + self.fibs[-1] <= self.maxN:
      self.fibs.append(self.fibs[-2] + self.fibs[-1])

  def findRepresentation(self, N):
    rest = N
    ind = len(self.fibs) - 1
    while rest: 
      while self.fibs[ind] > rest:
        ind -= 1
      yield self.fibs[ind]
      rest -= self.fibs[ind]
      ind -=2     

def main():
  g=sys.stdin
  #g = open("FIBOREP", "r") 
  s=g.read().splitlines()
  while '' in s: s.remove('')
  while '\n' in s: s.remove('\n') 
  fib = FibonacciRep()
  fib.calulateFib()
  for x in range(1, int(s[0]) + 1):
    print ' '.join(map(str, fib.findRepresentation(int(s[x]))))

if __name__=='__main__':
  main()