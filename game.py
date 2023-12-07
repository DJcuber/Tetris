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
    self.board = Board(self)
    
    
    self.currentPiece = pieces.IPiece(self.board)
    self.currentPiece.move((0, 0))
    
    
    self.board.board[4][0].state = 1 

    pieceList = [pieces.IPiece, pieces.OPiece, pieces.TPiece, pieces.SPiece, pieces.ZPiece, pieces.JPiece, pieces.LPiece]
    

    @self.main.keys.bindOnKey(action = "hDrop", ctx = self) #HAHAHHAHAHAHHAHAHAHHA
    def hDropBind(ctx):
      while not(ctx.currentPiece.move([0, -1])):
          pass
      ctx.currentPiece = pieceList[random.randint(0, 6)](ctx.board)

    @self.main.keys.bindOnKey(action = "rotClock", ctx = self)
    def rotClockBind(ctx):
      self.currentPiece.rotate(1)

    @self.main.keys.bindOnKey(action = "rotAnti", ctx = self)
    def rotClockBind(ctx):
      self.currentPiece.rotate(-1)
    
    while self.gameRunning and self.main.isModeRunning:
      
      display.window.blit(self.board.surface, ((display.windowSize[0] - display.windowSize[1]*10/24)/2, display.windowSize[1]*2/24))
      if self.main.keys.keyEvents["sDrop"]:
        self.currentPiece.move([0, -1])

      if self.main.keys.keyEvents["left"] and not(self.main.keys.keyEvents["right"]):
        self.currentPiece.move([-1, 0])
      
      elif self.main.keys.keyEvents["right"] and not(self.main.keys.keyEvents["left"]):
        self.currentPiece.move([1, 0])
      
      self.board.updateBoard()
      display.render()

      if self.main.eventHandle():
        return 1
      
      self.main.clock.tick(self.main.tickrate)
      
    self.main.isModeRunning = False
    return 0

  

class Board:
  def __init__(self, game) -> None:
    self.game: Game = game
    self.board: list[list[Square]] = [[Square(self) for i in range(22)] for i in range(10)]
    self.surface: pg.Surface = pg.Surface((self.game.main.display.windowSize[1]*10/24, self.game.main.display.windowSize[1]*20/24))
    self.surface.fill("#FFFFFF")
  
  def updateBoard(self) -> None:
    for i in range(10):
      for j in range(20): 
        if self.board[i][j].state == 0:
          self.board[i][j].surface.fill("#ffffff")
        else:
          self.board[i][j].surface.fill(Square.colors[self.board[i][j].state])
        self.surface.blit(self.board[i][j].surface, (i*self.game.main.display.windowSize[1]/24, self.game.main.display.windowSize[1] * 20/24 - (j+1)*self.game.main.display.windowSize[1]/24))

class Square:
  colors = [None, "#00ffff", "#ffff00", "#9900cc", "#00ff00", "#ff0000", "#0000ff", "#ff9900", "#999999"]
  def __init__ (self, board) -> None:
    self.board: Board = board
    self.surface: pg.Surface = pg.Surface((self.board.game.main.display.windowSize[1]/24, self.board.game.main.display.windowSize[1]/24))
    self.state: int = 0 #0: None, 1: Cyan, 2: Yellow, 3: Purple, 4: Green, 5: Red, 6: Blue, 7: Orange, 8: Gray

