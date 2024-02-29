import pygame as pg
import pieces
import gameOver
import random

class Game:
  def __init__(self, main) -> None:
    self.main: object = main
    self.gameRunning: bool = True
    self.actionQueue: list[list] = []
    self.gameLoop()

  def addAction(self, *args) -> None:
    self.actionQueue.append(args)

  def processActions(self) -> None:
    unique = []
    for i in self.actionQueue:
      if not(i in unique):
        unique.append(i)
    
    for i in unique: #IS VERY BROKEN NOT
      value = i[0](i[1])
      if i[0] == self.currentPiece.place or value == "place":
        if value == "place":
          self.currentPiece.place([None])
        self.currentBag.pop(0)
        self.currentPiece = self.currentBag[0](self.board)
        if len(self.currentBag) < 7:
          tempBag = [i for i in self.pieceList]
          random.shuffle(tempBag)
          for i in tempBag:
            self.currentBag.append(i)
        if self.currentPiece.move((0, 0)) == 1:
          self.main.isModeRunning = False #doesn't quit loop
          
    self.actionQueue = []
  

  def gameLoop(self) -> int:
    display = self.main.display
    display.window.fill("#FFF8F0")
    display.ui = []
    self.board: object = Board(self)

    self.score: int = 0
    #scoreUI = display.addElement((display.windowSize[0]/2, display.windowSize[1]*1/24), (display.windowSize[0]/2, display.windowSize[1]/24), "#FFF8F0", text="score:")
    scorePos = (display.windowSize[0]/2, display.windowSize[1]/24)
    scoreSize = (display.windowSize[0]/4, display.windowSize[1]/24)
    scoreSurface = pg.surface.Surface(scoreSize)
    
                                

    ticks = 0

    self.pieceList: list[object] = [pieces.IPiece, pieces.OPiece, pieces.TPiece, pieces.SPiece, pieces.ZPiece, pieces.JPiece, pieces.LPiece]
    self.currentBag: list[object] = [i for i in self.pieceList]
    random.shuffle(self.currentBag)
    self.currentPiece: object = self.currentBag[0](self.board)
    self.currentPiece.move((0, 0))
     

    @self.main.keys.bindOnKey(action = "hDrop", ctx = self) #HAHAHHAHAHAHHAHAHAHHA
    def hDropBind(ctx):
      self.addAction(self.currentPiece.place, [None])

    @self.main.keys.bindOnKey(action = "rotClock", ctx = self)
    def rotClockBind(ctx):
      ctx.currentPiece.rotate(1)

    @self.main.keys.bindOnKey(action = "rotAnti", ctx = self)
    def rotClockBind(ctx):
      ctx.currentPiece.rotate(-1)
    
    while self.gameRunning and self.main.isModeRunning:
      
      display.window.blit(self.board.surface, ((display.windowSize[0] - display.windowSize[1]*10/24)/2, display.windowSize[1]*2/24))
      if self.main.keys.keyEvents["sDrop"]:
        self.addAction(self.currentPiece.move, [0, -1])
        #self.currentPiece.move([0, -1])

      if self.main.keys.keyEvents["left"] and not(self.main.keys.keyEvents["right"]):
        self.addAction(self.currentPiece.move, [-1, 0])
        #self.currentPiece.move([-1, 0])
      
      elif self.main.keys.keyEvents["right"] and not(self.main.keys.keyEvents["left"]):
        self.addAction(self.currentPiece.move, [1, 0])
        #self.currentPiece.move([1, 0])

      scoreSurface.fill("#FFF8F0")
      scoreText = display.font.render(f"score: {self.score}", True, "#000000")
      scoreRect = scoreText.get_rect(center=(scoreSize[0]//2, scoreSize[1]//2))
      scoreSurface.blit(scoreText, scoreRect)
      display.window.blit(scoreSurface, scorePos)
      
      self.board.updateBoard()
      display.render()

      if self.main.eventHandle():
        return 1
      
      self.main.clock.tick(self.main.tickrate)
      ticks += 1
      
      if (ticks % (self.main.tickrate / 16)) == 0: #16 times a sec, ticks % (tickrate / 2)
        self.processActions()

      if (ticks % (self.main.tickrate / 2)) == 0: #2 times a sec
        self.addAction(self.currentPiece.move, [0, -1])

      if ticks == self.main.tickrate:
        ticks = 0
        
    self.main.mode = "game over"
    gameOverScene = gameOver.GameOver(self.main, self.score)
    
    return 0

  

class Board:
  def __init__(self, game) -> None:
    self.game: Game = game
    self.board: list[list[Square]] = [[Square(self) for i in range(22)] for i in range(10)]
    self.surface: pg.Surface = pg.Surface((self.game.main.display.windowSize[1]*10/24, self.game.main.display.windowSize[1]*22/24)) #CHANGE THESE NUMBERS
    self.surface.fill("#FFFFFF")
  
  def updateBoard(self) -> None:
    for i in range(10):
      for j in range(22):  #22
        if self.board[i][j].state == 0:
          self.board[i][j].surface.fill("#ffffff")
        else:
          self.board[i][j].surface.fill(Square.colors[self.board[i][j].state])
        self.surface.blit(self.board[i][j].surface, (i*self.game.main.display.windowSize[1]/24, self.game.main.display.windowSize[1] * 22/24 - (j+1)*self.game.main.display.windowSize[1]/24)) #AND HERE

  def clearRow(self, rows) -> None:
    linesCleared = 0
    for rowIndex in range(len(rows)):
      
      for column in self.board:
        if column[rows[rowIndex]].state == 0:
          break
      else:
        #Line is cleared
        for column in range(10):
          for row in range(rows[rowIndex], 21):
            self.board[column][row] = self.board[column][row+1]
          self.board[column][21] = Square(self)
        linesCleared += 1
        rows = [i - 1 for i in rows]
    self.updateBoard()
    
    if linesCleared == 1:
      self.game.score += 40
    elif linesCleared == 2:
      self.game.score += 100
    elif linesCleared == 3:
      self.game.score += 300
    elif linesCleared == 4:
      self.game.score += 1200

  

class Square:
  colors = [None, "#00ffff", "#ffff00", "#9900cc", "#00ff00", "#ff0000", "#0000ff", "#ff9900", "#999999"]
  def __init__ (self, board) -> None:
    self.board: object = board
    self.surface: object = pg.Surface((self.board.game.main.display.windowSize[1]/24, self.board.game.main.display.windowSize[1]/24))
    self.state: int = 0 #0: None, 1: Cyan, 2: Yellow, 3: Purple, 4: Green, 5: Red, 6: Blue, 7: Orange, 8: Gray

