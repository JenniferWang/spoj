#https://vijos.org/p/1002
import sys
class Frogleap():
  def __init__(self, length, stones, min_step, max_step):
    self.length = length + max_step # Attention
    self.stones = stones
    self.stones.sort()
    self.min_step = min_step
    self.max_step = max_step

  def pruneLength(self):
    """
    When dist >= (min_step + 1) * max_step, dist can be represented as 
    n * min_step + a + m * max_step, where a is 0 or min_step < a < max_step
    and we can prove that this representation can be modified to have n > 0, thus
    we can always do dist -= min_step
    """
    stops = [0] + self.stones + [self.length]
    pruned_stops = [0]
    for idx in range(1, len(stops)):
      dist = stops[idx] - stops[idx - 1]
      if dist > (self.min_step + 1) * self.max_step:
        dist -= ((dist - (self.min_step + 1) * self.max_step) / self.min_step) * self.min_step
      pruned_stops.append(dist + pruned_stops[-1])
    self.stones = pruned_stops[1: -1]
    self.length = pruned_stops[-1]

  def findMinStones(self):
    """
    dp[m] = minimum # stones when landed exactly at m
    TODO: for loop is too long
    """
    self.pruneLength()
    min_stones = [0]
    for curr_pos in range(1, self.length + 1): # 1, 2, 3, ..., L + max_step
      curr_min = self.length
      if min_stones[max(0, curr_pos - self.max_step): max(-1, curr_pos - self.min_step) + 1]:
        curr_min = min(min_stones[max(0, curr_pos - self.max_step): max(-1, curr_pos - self.min_step) + 1])\
        + int(curr_pos in self.stones)
      if curr_pos >= self.min_step and curr_pos <= self.max_step:
        curr_min = int(curr_pos in self.stones)
      min_stones.append(curr_min)
    print min(min_stones[self.length: self.length - self.max_step: -1])

def main():
  #g=sys.stdin
  g = open("FROGLEAP", "r") 
  length = int(g.readline())
  sec_line = map(int, g.readline().split())
  min_step = sec_line[0]
  max_step = sec_line[1]
  num_stones = sec_line[2]
  stones = map(int, g.readline().split())
  Frogleap(length, stones, min_step, max_step).findMinStones()

if __name__=='__main__':
  main()