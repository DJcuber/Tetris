import pygame as pg
import json

class Main:
  def __init__(self) -> None:
    pg.init()
    self.windowSize = (800, 600)
    self.window: pg.Surface = pg.display.set_mode(self.windowSize)
    self.clock: pg.time.Clock = pg.time.Clock()
    self.tickrate: int = 16
    self.isRunning: bool = True
    self.keys: Keys = Keys()
    self.game: Game = Game(self)

  def eventHandle(self) -> int:
    for ev in pg.event.get():
      if ev.type == pg.QUIT:
        self.isRunning = False
        return 1
      
      elif ev.type == pg.KEYDOWN:
        for i, j in self.keys.binds.items():
          if ev.key == j:
            self.keys.keyEvents[i] = True
      
      elif ev.type == pg.KEYUP:
        for i, j in self.keys.binds.items():
          if ev.key == j:
            self.keys.keyEvents[i] = False
    return 0

class Keys:
  def __init__(self):
    with open("options.json", "r") as f:
      self.binds: dict = json.loads(f.read())["keybinds"]
    for i in self.binds:
      self.binds[i] = eval("pg." + self.binds[i])
    self.keyEvents = {i:False for i in ("left", "right", "hDrop", "sDrop", "hold", "rotClock", "rotAnti")}

class Game:
  def __init__(self, main) -> None:
    self.main: Main = main
    self.gameRunning: bool = True
    self.gameLoop()

  def gameLoop(self) -> int:
    board = Board(self.main)
    testPiece = Piece(board)
    testPiece.color = 1 
    testPiece.squarePos = [[3, 19], [4, 19], [5, 19], [6, 19]]
    testPiece.move([0, 0])
    board.board[4][0].state = 2 #and here breaks everything
    testPiece.move([0, 0])

    while self.gameRunning:
      self.main.window.blit(board.surface, ((self.main.windowSize[0] - self.main.windowSize[1]*10/24)/2, self.main.windowSize[1]*2/24))
      if self.main.keys.keyEvents["sDrop"]:
        testPiece.move([0, -1])

      pg.display.flip()
      if self.main.eventHandle():
        return 1
      self.main.clock.tick(self.main.tickrate)
    return 0
  
class Board:
  def __init__(self, main) -> None:
    self.main: Main = main
    self.board: list[list[Square]] = [[Square(self.main) for i in range(22)] for i in range(10)]
    self.surface: pg.Surface = pg.Surface((self.main.windowSize[1]*10/24, self.main.windowSize[1]*20/24))
    self.surface.fill("#FFFFFF")
  
  def updateBoard(self) -> None:
    for i in range(10):
      for j in range(20): 
        if self.board[i][j].state == 0:
          self.board[i][j].surface.fill("#ffffff")
        else:
          self.board[i][j].surface.fill(Square.colors[self.board[i][j].state])
        self.surface.blit(self.board[i][j].surface, (i*self.main.windowSize[1]/24, self.main.windowSize[1] * 20/24 - (j+1)*self.main.windowSize[1]/24))

class Square:
  colors = [None, "#00ffff", "#ffff00", "#9900cc", "#00ff00", "#ff0000", "#0000ff", "#ff9900", "#999999"]
  def __init__ (self, main) -> None:
    self.main: Main = main
    self.surface: pg.Surface = pg.Surface((self.main.windowSize[1]/24, self.main.windowSize[1]/24))
    self.state: int = 0 #0: None, 1: Cyan, 2: Yellow, 3: Purple, 4: Green, 5: Red, 6: Blue, 7: Orange, 8: Gray

class Piece:
  def __init__(self, board) -> None:
    self.board: Board = board
    self.squarePos: list[list[int]] = [[0 for i in range(2)] for i in range(4)]
    self.color = 0
  
  def move(self, dir) -> int:
    newPos: list[list[int]] = [[i[0]+dir[0], i[1]+dir[1]] for i in self.squarePos]
    oldStates: list[int] = [0 for i in range(4)]
    for i, j in enumerate(self.squarePos):

      oldStates[i] = self.board.board[j[0]][j[1]].state
      self.board.board[j[0]][j[1]].state = 0
    
    for i in newPos:
      if not(0 <= i[0] <= 10 and 0 <= i[1] <= 22) or self.board.board[i[0]][i[1]].state != 0:
        for j, k in enumerate(self.squarePos):
          self.board.board[k[0]][k[1]].state = oldStates[j]
        self.board.updateBoard()
        return 1
    
    self.squarePos = newPos
    for i in self.squarePos:
      self.board.board[i[0]][i[1]].state = self.color
    self.board.updateBoard()
    return 0
      

def main():
  instance = Main()

if __name__ == "__main__":
  main()
  #piece = Piece(None)
  #piece.move([1, 2])



