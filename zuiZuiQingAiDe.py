class Board():
  def __init__(self, board):
    self.board = board

  def findMaxProduct(self):
    if not self.board:
      return
    maxProds = []
    minProds = []

    for row in self.board:
      pre_max = maxProds
      pre_min = minProds
      maxProds = []
      minProds = []
      for colIdx, cell in enumerate(row):
        if pre_max and maxProds:
          if cell > 0:
            maxProds.append(max(cell * pre_max[colIdx], cell * maxProds[-1]))
            minProds.append(min(cell * pre_min[colIdx], cell * minProds[-1]))
          else:
            maxProds.append(max(cell * pre_min[colIdx], cell * minProds[-1]))
            maxProds.append(min(cell * pre_max[colIdx], cell * maxProds[-1]))
        elif pre_max:
          if cell > 0:
            maxProds.append(cell * pre_max[colIdx])
            minProds.append(cell * pre_min[colIdx])
          else:
            maxProds.append(cell * pre_min[colIdx])
            minProds.append(cell * pre_max[colIdx])
        else:
          if cell > 0:
            maxProds.append(cell)
            minProds.append(float('inf'))
          else:
            maxProds.append(float('-inf'))
            minProds.append(cell)

    return max(maxProds[-1], minProds[-1]) 

def test():
  boards = [ 
    [[1]], 
    [[0]], 
    [[-1]], 
    [[1, -3],[3, -3]], 
    [[-3, 2], [1, -1]], 
    [[1, 2], [3, 4]], 
    [[-1, -2], [-3, -4]], 
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]],
  ]
  ans = [1, 0, -1, 9, 6, 12, -8, 9*8*7*4*1, -1*2*3*6*9]
  for i, board in enumerate(boards):
    if Board(board).findMaxProduct() == ans[i]:
      continue
    print board, ans[i], Board(board).findMaxProduct()


if __name__ == '__main__':
  test()


