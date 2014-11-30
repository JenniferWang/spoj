from pprint import pprint as pp
def sizeMaxSubSquare(Matrix):
  """
  http://www.geeksforgeeks.org/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/
  This O(m * n) algorithm cannot extended to calculating rectangles as the max length of the 
  sides won't necessarily yield the max area of a rectangle
  input: bool matrix
  """
  m = len(Matrix)
  n = len(Matrix[0])
  maxSubs = [[None for y in range(n)] for x in range(m)]

  for col in range(n):
    maxSubs[0][col] = Matrix[0][col]
  for row in range(m):
    maxSubs[row][0] = Matrix[row][0]

  for col in range(1, n):
    for row in range(1, m):
      if Matrix[row][col] == 1:
        maxSubs[row][col] = min(maxSubs[row - 1][col - 1], \
          maxSubs[row - 1][col], maxSubs[row][col - 1]) + 1
      else:
        maxSubs[row][col] = 0
  #pp(maxSubs)
  maxSize = 0
  for row in maxSubs:
    maxSize = max(maxSize, max(row))
  return maxSize

matrix = [[0, 1, 1, 0, 1],
          [1, 1, 0, 1, 0],
          [0, 1, 1, 1, 0],
          [1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0]]
print sizeMaxSubSquare(matrix)
