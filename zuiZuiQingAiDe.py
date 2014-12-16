class Board():
  def __init__(self, board):
    self.board = board

  def findMaxProductGyz(self):
    if not self.board:
      return 1
    max_prods = [1]
    min_prods = [1]    
    for row in self.board:
      last_max_prods = max_prods
      last_min_prods = min_prods
      max_prods = []
      min_prods = [] 
      for col_ind, cell_val in enumerate(row):
        potential_prods = []
        if max_prods: 
          potential_prods += [cell_val * max_prods[-1], cell_val * min_prods[-1]]
        if len(last_max_prods) > col_ind:
          potential_prods.append(cell_val * last_max_prods[col_ind])
          potential_prods.append(cell_val * last_min_prods[col_ind])
        max_prods.append(max(potential_prods))
        min_prods.append(min(potential_prods))
    return max_prods[-1]

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
    if Board(board).findMaxProductGyz() == ans[i]:
      continue
    print board, ans[i], Board(board).findMaxProductGyz()


if __name__ == '__main__':
  test()


