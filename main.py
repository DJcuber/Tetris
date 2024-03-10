import pygame as pg
import json
import menu
import game
import keys
import ui
import logIn
import leaderboard
import db

class Main:
  def __init__(self) -> None:
    self.mode: str = "login"
    self.isRunning: bool = True
    self.isModeRunning: bool = True
    self.db: object = None
    self.mainLoop()

  def initPg(self) -> None:
    pg.init()
    self.display: object = ui.Display()
    self.clock: object = pg.time.Clock()
    self.tickrate: int = 32
    self.keys: object = keys.Keys()

  def eventHandle(self) -> int:
    for ev in pg.event.get():
      if ev.type == pg.QUIT:
        self.isRunning = False
        self.isModeRunning = False
        return 1
      
      elif ev.type == pg.KEYDOWN:
        for i, j in self.keys.binds.items():
          if ev.key == j:
            self.keys.keyEvents[i] = True
            for bind in self.keys.keyFunc:
              if bind == i:
                self.keys.keyFunc[bind](self.keys.ctx)
      
      elif ev.type == pg.KEYUP:
        for i, j in self.keys.binds.items():
          if ev.key == j:
            self.keys.keyEvents[i] = False
      
      elif ev.type == pg.MOUSEBUTTONDOWN:
        self.display.clickEvent((True, ev.pos, ev.button))

      elif ev.type == pg.MOUSEBUTTONUP:
        self.display.clickEvent((False, ev.pos, ev.button))

    return 0

  def mainLoop(self) -> None:
    while self.isRunning:
      self.isModeRunning = True
      if self.mode == "menu":
        menu.Menu(self)
      elif self.mode == "game":
        game.Game(self)
      elif self.mode == "login":
        self.db = db.Database(self)
        login = logIn.LogIn(self)
        self.db.connect()
        self.initPg()
      elif self.mode == "leaderboard":
        leaderboard.Leaderboard(self)
      else:
        self.isRunning = False
    pg.quit()

def main() -> None:
  instance = Main()

if __name__ == "__main__":
  main()
  
#lines of python code: 725