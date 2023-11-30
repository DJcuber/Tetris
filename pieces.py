class Piece:
  def __init__(self, board) -> None:
    self.board: object = board
    self.piecePos = [3, 18]
    self.squarePos: list[list[list[int]]] = [[[0 for i in range(2)] for i in range(4)] for i in range(4)]
    self.rotation = 0
    self.color = 0
  
  def move(self, direction) -> int:
    newPos: list[list[int]] = [[i[0]+direction[0]+self.piecePos[0], i[1]+direction[1]+self.piecePos[1]] for i in self.squarePos[self.rotation]]
    oldStates: list[int] = [0 for i in range(4)]
    for i, j in enumerate(self.squarePos[self.rotation]):

      oldStates[i] = self.board.board[j[0]+self.piecePos[0]][j[1]+self.piecePos[1]].state
      self.board.board[j[0]+self.piecePos[0]][j[1]+self.piecePos[1]].state = 0
    
    for i in newPos:
      if not(0 <= i[0] <= 9 and 0 <= i[1] <= 21): 
        for j, k in enumerate(self.squarePos[self.rotation]):
          self.board.board[k[0]+self.piecePos[0]][k[1]+self.piecePos[1]].state = oldStates[j]
        self.board.updateBoard()
        return 1

      elif self.board.board[i[0]][i[1]].state != 0:
        for j, k in enumerate(self.squarePos[self.rotation]):
          self.board.board[k[0]+self.piecePos[0]][k[1]+self.piecePos[1]].state = oldStates[j]
        self.board.updateBoard()
        return 1

    self.piecePos = [self.piecePos[0]+direction[0], self.piecePos[1]+direction[1]]
    for i in self.squarePos[self.rotation]:
      self.board.board[i[0]+self.piecePos[0]][i[1]+self.piecePos[1]].state = self.color
    self.board.updateBoard()
    return 0

    def rotate(self, direction):
        
      newRotation += direction
      newRotation %= 4
      
      
    
    

class IPiece(Piece):
  def __init__(self, board) -> None:
    super().__init__(board)
    self.color = 1
    self.squarePos = [[[0, 2], [1, 2], [2, 2], [3, 2]],
                      [[2, 0], [2, 1], [2, 2], [2, 3]],
                      [[0, 1], [1, 1], [2, 1], [3, 1]],
                      [[1, 0], [1, 1], [1, 2], [1, 3]]
                      ]
    self.rotation = 0
    

class OPiece(Piece):
  def __init__(self, board) -> None:
    super().__init__(board)
    self.color = 2
    self.squarePos = [[[1, 2], [1, 3], [2, 2], [2, 3]]] #[[1, 2], [1, 3], [2, 2], [2, 3]]

class TPiece(Piece):
  def __init__(self, board) -> None:
    super().__init__(board)
    self.color = 3
    self.squarePos = [[[0, 2], [1, 2], [1, 3], [2, 2]]] #[[0, 2], [1, 2], [1, 3], [2, 2]]

class SPiece(Piece):
  def __init__(self, board) -> None:
    super().__init__(board)
    self.color = 4
    self.squarePos = [[[0, 2], [1, 2], [1, 3], [2, 3]]] #[[0, 2], [1, 2], [1, 3], [2, 3]]

class ZPiece(Piece):
  def __init__(self, board) -> None:
    super().__init__(board)
    self.color = 5
    self.squarePos = [[[0, 3], [1, 3], [1, 2], [2, 2]]] #[[0, 3], [1, 3], [1, 2], [2, 2]]

class JPiece(Piece):
  def __init__(self, board) -> None:
    super().__init__(board)
    self.color = 6
    self.squarePos = [[[0, 3], [0, 2], [1, 2], [2, 2]]] #[[0, 3], [0, 2], [1, 2], [2, 2]]

class LPiece(Piece):
  def __init__(self, board) -> None:
    super().__init__(board)
    self.color = 7
    self.squarePos = [[[0, 2], [1, 2], [2, 2], [2, 3]]] #[[0, 2], [1, 2], [2, 2], [2, 3]]


#0: None, 1: Cyan, 2: Yellow, 3: Purple, 4: Green, 5: Red, 6: Blue, 7: Orange, 8: Gray
