class Piece:
  def __init__(self, board) -> None:
    self.board: object = board
    self.squarePos: list[list[int]] = [[0 for i in range(2)] for i in range(4)]
    self.color = 0
  
  def move(self, dir) -> int:
    newPos: list[list[int]] = [[i[0]+dir[0], i[1]+dir[1]] for i in self.squarePos]
    oldStates: list[int] = [0 for i in range(4)]
    for i, j in enumerate(self.squarePos):

      oldStates[i] = self.board.board[j[0]][j[1]].state
      self.board.board[j[0]][j[1]].state = 0
    
    for i in newPos:
      if not(0 <= i[0] <= 9 and 0 <= i[1] <= 21): 
        for j, k in enumerate(self.squarePos):
          self.board.board[k[0]][k[1]].state = oldStates[j]
        self.board.updateBoard()
        return 1

      elif self.board.board[i[0]][i[1]].state != 0:
        for j, k in enumerate(self.squarePos):
          self.board.board[k[0]][k[1]].state = oldStates[j]
        self.board.updateBoard()
        return 1
    
    
    self.squarePos = newPos
    for i in self.squarePos:
      self.board.board[i[0]][i[1]].state = self.color
    self.board.updateBoard()
    return 0

class IPiece(Piece):
  def __init__(self, board) -> None:
    super().__init__(board)
    self.color = 1
    self.squarePos = [[3, 20], [4, 20], [5, 20], [6, 20]]

class OPiece(Piece):
  def __init__(self, board) -> None:
    super().__init__(board)
    self.color = 2
    self.squarePos = [[4, 20], [4, 21], [5, 20], [5, 21]]

class TPiece(Piece):
  def __init__(self, board) -> None:
    super().__init__(board)
    self.color = 3
    self.squarePos = [[3, 20], [4, 20], [4, 21], [5, 20]]

class SPiece(Piece):
  def __init__(self, board) -> None:
    super().__init__(board)
    self.color = 4
    self.squarePos = [[3, 20], [4, 20], [4, 21], [5, 21]]

class ZPiece(Piece):
  def __init__(self, board) -> None:
    super().__init__(board)
    self.color = 5
    self.squarePos = [[3, 21], [4, 21], [4, 20], [5, 20]]

class JPiece(Piece):
  def __init__(self, board) -> None:
    super().__init__(board)
    self.color = 6
    self.squarePos = [[3, 21], [3, 20], [4, 20], [5, 20]]

class LPiece(Piece):
  def __init__(self, board) -> None:
    super().__init__(board)
    self.color = 7
    self.squarePos = [[3, 20], [4, 20], [5, 20], [5, 21]]


#0: None, 1: Cyan, 2: Yellow, 3: Purple, 4: Green, 5: Red, 6: Blue, 7: Orange, 8: Gray