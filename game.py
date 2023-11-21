import pygame as pg
import pieces
import random

class Game:
  def __init__(self, main) -> None:
    self.main = main
    self.gameRunning: bool = True
    self.gameLoop()

  def gameLoop(self) -> int:
    display = self.main.display
    display.window.fill("#FFF8F0")
    display.ui = []
    board = Board(self.main)
    currentPiece = pieces.TPiece(board)
    board.board[4][0].state = 1 

    pieceList = [pieces.IPiece, pieces.OPiece, pieces.TPiece, pieces.SPiece, pieces.ZPiece, pieces.JPiece, pieces.LPiece]

    while self.gameRunning:
      display.window.blit(board.surface, ((display.windowSize[0] - display.windowSize[1]*10/24)/2, display.windowSize[1]*2/24))
      if self.main.keys.keyEvents["sDrop"]:
        currentPiece.move([0, -1])
      
      if self.main.keys.keyEvents["hDrop"]:
        while not(currentPiece.move([0, -1])):
          pass
        currentPiece = pieceList[random.randint(0, 6)](board)


      if self.main.keys.keyEvents["left"] and not(self.main.keys.keyEvents["right"]):
        currentPiece.move([-1, 0])
      
      elif self.main.keys.keyEvents["right"] and not(self.main.keys.keyEvents["left"]):
        currentPiece.move([1, 0])
      
      board.updateBoard()
      display.render()

      if self.main.eventHandle():
        return 1
      
      self.main.clock.tick(self.main.tickrate)
    return 0

class Board:
  def __init__(self, main) -> None:
    self.main: main.Main = main
    self.board: list[list[Square]] = [[Square(self.main) for i in range(22)] for i in range(10)]
    self.surface: pg.Surface = pg.Surface((self.main.display.windowSize[1]*10/24, self.main.display.windowSize[1]*20/24))
    self.surface.fill("#FFFFFF")
  
  def updateBoard(self) -> None:
    for i in range(10):
      for j in range(20): 
        if self.board[i][j].state == 0:
          self.board[i][j].surface.fill("#ffffff")
        else:
          self.board[i][j].surface.fill(Square.colors[self.board[i][j].state])
        self.surface.blit(self.board[i][j].surface, (i*self.main.display.windowSize[1]/24, self.main.display.windowSize[1] * 20/24 - (j+1)*self.main.display.windowSize[1]/24))

class Square:
  colors = [None, "#00ffff", "#ffff00", "#9900cc", "#00ff00", "#ff0000", "#0000ff", "#ff9900", "#999999"]
  def __init__ (self, main) -> None:
    self.main: main.Main = main
    self.surface: pg.Surface = pg.Surface((self.main.display.windowSize[1]/24, self.main.display.windowSize[1]/24))
    self.state: int = 0 #0: None, 1: Cyan, 2: Yellow, 3: Purple, 4: Green, 5: Red, 6: Blue, 7: Orange, 8: Gray

