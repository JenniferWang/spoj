 import pprint
def maxSubArraySum(L):
  """
  Given an 1-D array, return the maximum sum of contiguous subarray
  http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
  recursion relation is a little tricky
  """
  n = len(L)
  if n == 0:
    return None
  curr_sum = L[0] # Just update the latest is ok, don't need to store
  max_sum = curr_sum
  for end in xrange(1, n):
    curr_sum = max(curr_sum + L[end], L[end])
    max_sum = max(max_sum, curr_sum)
  return max_sum

# print maxSubArraySum([-2, -3, 4, -1, -2, 1, 5, -3])
# print maxSubArraySum([-2, -1])
# print maxSubArraySum([-2, -1, 0])

def findMaxSum(matrix):
  """
  http://www.geeksforgeeks.org/dynamic-programming-set-27-max-sum-rectangle-in-a-2d-matrix/
  """
  if matrix == [[]]:
    return None
  m = len(matrix) # row
  n = len(matrix[0])
  maxSum = matrix[0][0]
  sub_row_sum = [[[] for col_right in xrange(n)] for col_left in xrange(n)]
  for col in xrange(n):
    sub_row_sum[col][col] = [matrix[row][col] for row in xrange(m)]

  for width in xrange(2, n + 1):
    for col in xrange(n - width + 1):
      sub_row_sum[col][col + width - 1] = [sub_row_sum[col][col + width - 2][x] + \
        sub_row_sum[col + width - 1][col + width - 1][x] for x in xrange(m)]
      maxSum = max(maxSum, maxSubArraySum(sub_row_sum[col][col + width - 1]))
  return maxSum

print findMaxSum([[1, 2, -1, -4, -20],
                  [-8, -3, 4, 2, 1],
                  [3, 8, 10, 1, 3],
                  [-4, -1, 1, 7, -6]])