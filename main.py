import pygame as pg
import json

class Main:
  def __init__(self) -> None:
    pg.init()
    self.windowSize = (800, 600)
    self.window: pg.Surface = pg.display.set_mode(self.windowSize)
    self.clock: pg.time.Clock = pg.time.Clock()
    self.tickrate: int = 64
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
    board.board[0][0].state = 1
    board.updateBoard()
    while self.gameRunning:
      self.main.window.blit(board.surface, ((self.main.windowSize[0] - self.main.windowSize[1]*10/24)/2, self.main.windowSize[1]*2/24))

      pg.display.flip()
      if self.main.eventHandle():
        return 1
      self.main.clock.tick(self.main.tickrate)
    return 0
  
class Board:
  def __init__(self, main) -> None:
    self.main: Main = main
    self.board: list[list[Square]] = [[Square(self.main) for i in range(10)] for i in range(22)]
    self.surface: pg.Surface = pg.Surface((self.main.windowSize[1]*10/24, self.main.windowSize[1]*20/24))
    self.surface.fill("#FFFFFF")
  
  def updateBoard(self) -> None:
    for i in range(20):
      for j, w in enumerate(self.board[i]):
        if w.state == 0:
          w.surface.set_alpha(0)
        else:
          w.surface.fill(Square.colors[w.state])
        self.surface.blit(w.surface, (j*self.main.windowSize[1]/24, self.main.windowSize[1] * 20/24 - (i+1)*self.main.windowSize[1]/24))

class Square:
  colors = [None, "#00ffff", "#ffff00", "#9900cc", "#00ff00", "#ff0000", "#0000ff", "#ff9900", "#999999"]
  def __init__ (self, main) -> None:
    self.main: Main = main
    self.surface: pg.Surface = pg.Surface((self.main.windowSize[1]/24, self.main.windowSize[1]/24))
    self.state: int = 0 #0: None, 1: Cyan, 2: Yellow, 3: Purple, 4: Green, 5: Red, 6: Blue, 7: Orange, 8: Gray
  

def main():
  instance = Main()

if __name__ == "__main__":
  main()

