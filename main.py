import pygame as pg
import json
import menu
import game
import keys
import ui

class Main:
  def __init__(self) -> None:
    pg.init()
    self.display: ui.Display = ui.Display()
    self.clock: pg.time.Clock = pg.time.Clock()
    self.tickrate: int = 16
    self.isRunning: bool = True
    self.keys: keys.Keys = keys.Keys()
    self.game: game.Game = game.Game(self)

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
      
      elif ev.type == pg.MOUSEBUTTONDOWN:
        self.display.clickEvent((True, ev.pos, ev.button))

    return 0


def main():
  instance = Main()

if __name__ == "__main__":
  main()
  
