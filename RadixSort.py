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
    count = [0 for x in xrange(self.base)]
    for value in self.sorted:
      count[(value / exp) % self.base] += 1
    new_index = [0]
    for x in xrange(1, self.base):
      new_index.append(count[x - 1] + new_index[-1])
    curr_data = [None for value in self.sorted]
    for value in self.sorted:
      remain = (value / exp) % self.base
      index = new_index[remain]
      curr_data[index] = value
      new_index[remain] += 1
    self.sorted = curr_data

  def radixSort(self):
    exp = 1
    max_data = self.getMax()
    self.sorted = self.data[:]
    while max_data / exp != 0:
      self.countingSort(exp)
      exp *= self.base
    return self.sorted

countingsort = RadixSort([3, 2, 1, 9, 8], 2)
print countingsort.radixSort()

