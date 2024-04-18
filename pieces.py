class Piece:
  def __init__(self, board) -> None:
    self.board: object = board
    self.piecePos: list[int] = [3, 18]
    #The shape of each piece is defined by a 2d array consisting of the relative coordinates of each square and a list of all the coordinates.
    #It stores this for all possible rotations in a 3d array.
    self.squarePos: list[list[list[int]]] = [[[0 for i in range(2)] for i in range(4)] for i in range(4)]

    self.rotation = 0
    self.color = 0
    
  
  def move(self, direction) -> int:
    newPos: list[list[int]] = [[i[0]+direction[0]+self.piecePos[0], i[1]+direction[1]+self.piecePos[1]] for i in self.squarePos[self.rotation]]
    

    #Removes old piece from the board
    for i in self.squarePos[self.rotation]:
      if self.board.board[i[0]+self.piecePos[0]][i[1]+self.piecePos[1]].state != 0 and self.board.board[i[0]+self.piecePos[0]][i[1]+self.piecePos[1]].state != self.color:
        return 1
      self.board.board[i[0]+self.piecePos[0]][i[1]+self.piecePos[1]].state = 0 
    
    for i in newPos:
      if not(0 <= i[0] <= 9 and 0 <= i[1] <= 21): #checks if the new position is off the screen
        #converts board back to it's previous state
        for j, k in enumerate(self.squarePos[self.rotation]):
          self.board.board[k[0]+self.piecePos[0]][k[1]+self.piecePos[1]].state = self.color
        self.board.updateBoard()
        if i[1] < 0: #if the piece reached the bottom of the screen, place the piece
          return "place"
        return 1

      elif self.board.board[i[0]][i[1]].state != 0: #if collided with another piece
        #converts board back to it's previous state
        for j, k in enumerate(self.squarePos[self.rotation]):
          self.board.board[k[0]+self.piecePos[0]][k[1]+self.piecePos[1]].state = self.color
        self.board.updateBoard()
        if direction[1] == -1: #if the piece was moving down when it touched another piece, place it
          return "place"
        return 1

    self.piecePos = [self.piecePos[0]+direction[0], self.piecePos[1]+direction[1]] #updates position of the piece

    #places the piece
    for i in self.squarePos[self.rotation]:
      self.board.board[i[0]+self.piecePos[0]][i[1]+self.piecePos[1]].state = self.color
    self.board.updateBoard()
    return 0

  def rotate(self, direction) -> int:
      
    newRotation = self.rotation + direction
    newRotation %= 4

    newPos = [[i[0]+self.piecePos[0], i[1]+self.piecePos[1]] for i in self.squarePos[newRotation]]
      
    for i in self.squarePos[self.rotation]:
      self.board.board[i[0]+self.piecePos[0]][i[1]+self.piecePos[1]].state = 0 #Removes old piece

    for i in newPos:
      if not(0 <= i[0] <= 9 and 0 <= i[1] <= 21): #checks if the new position is still on the screen
        #adds old pieces back to the screen
        for j, k in enumerate(self.squarePos[self.rotation]):
          self.board.board[k[0]+self.piecePos[0]][k[1]+self.piecePos[1]].state = self.color
        self.board.updateBoard()
        return 1

      #checks if the new position is occupied by a piece
      elif self.board.board[i[0]][i[1]].state != 0:
        for j, k in enumerate(self.squarePos[self.rotation]):
          self.board.board[k[0]+self.piecePos[0]][k[1]+self.piecePos[1]].state = self.color
        self.board.updateBoard()
        return 1

    #update board to add piece with new position
    self.rotation = newRotation
    for i in self.squarePos[self.rotation]:
      self.board.board[i[0]+self.piecePos[0]][i[1]+self.piecePos[1]].state = self.color #error
    self.board.updateBoard()
    return 0

  def place(self, *args) -> None:
    while not(self.move([0, -1])): #moves the piece down until it cannot move further
      pass
    #find what rows the piece occupies and then checks if the lines have been cleared.
    rows = [i[1] + self.piecePos[1] for i in self.squarePos[self.rotation]]
    self.board.clearRow(rows)
    
      
#Defines the shape of each piece in each rotation, and the colour of each piece
    

class IPiece(Piece):
  def __init__(self, board) -> None:
    super().__init__(board)
    self.color = 1
    self.squarePos = [
                      [[0, 2], [1, 2], [2, 2], [3, 2]],
                      [[2, 0], [2, 1], [2, 2], [2, 3]],
                      [[0, 1], [1, 1], [2, 1], [3, 1]],
                      [[1, 0], [1, 1], [1, 2], [1, 3]]
                      ]
    
class OPiece(Piece):
  def __init__(self, board) -> None:
    super().__init__(board)
    self.color = 2
    self.squarePos = [
                      [[1, 2], [1, 3], [2, 2], [2, 3]],
                      [[1, 2], [1, 3], [2, 2], [2, 3]],
                      [[1, 2], [1, 3], [2, 2], [2, 3]],
                      [[1, 2], [1, 3], [2, 2], [2, 3]]
                      ]

class TPiece(Piece):
  def __init__(self, board) -> None:
    super().__init__(board)
    self.color = 3
    self.squarePos = [
                      [[0, 2], [1, 2], [1, 3], [2, 2]],
                      [[1, 3], [1, 2], [1, 1], [2, 2]],
                      [[0, 2], [1, 2], [1, 1], [2, 2]],
                      [[0, 2], [1, 2], [1, 3], [1, 1]]
                      ]

class SPiece(Piece):
  def __init__(self, board) -> None:
    super().__init__(board)
    self.color = 4
    self.squarePos = [
                      [[0, 2], [1, 2], [1, 3], [2, 3]],
                      [[1, 3], [1, 2], [2, 2], [2, 1]],
                      [[0, 1], [1, 1], [1, 2], [2, 2]],
                      [[0, 3], [0, 2], [1, 2], [1, 1]]
                      ]

class ZPiece(Piece):
  def __init__(self, board) -> None:
    super().__init__(board)
    self.color = 5
    self.squarePos = [
                      [[0, 3], [1, 3], [1, 2], [2, 2]],
                      [[1, 1], [1, 2], [2, 2], [2, 3]],
                      [[0, 2], [1, 2], [1, 1], [2, 1]],
                      [[0, 1], [0, 2], [1, 2], [1, 3]]
                      ]

class JPiece(Piece):
  def __init__(self, board) -> None:
    super().__init__(board)
    self.color = 6
    self.squarePos = [
                      [[0, 3], [0, 2], [1, 2], [2, 2]],
                      [[1, 1], [1, 2], [1, 3], [2, 3]],
                      [[0, 2], [1, 2], [2, 2], [2, 1]],
                      [[0, 1], [1, 1], [1, 2], [1, 3]]
                      ]

class LPiece(Piece):
  def __init__(self, board) -> None:
    super().__init__(board)
    self.color = 7
    self.squarePos = [
                      [[0, 2], [1, 2], [2, 2], [2, 3]],
                      [[1, 3], [1, 2], [1, 1], [2, 1]],
                      [[0, 1], [0, 2], [1, 2], [2, 2]],
                      [[0, 3], [1, 3], [1, 2], [1, 1]]
                      ]


#0: None, 1: Cyan, 2: Yellow, 3: Purple, 4: Green, 5: Red, 6: Blue, 7: Orange, 8: Gray
