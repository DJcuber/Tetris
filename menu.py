import pygame as pg
import ui

class Menu:
  def __init__(self, main) -> None:
    self.main = main
    self.menuRunning = True
    self.menuLoop()

  def menuLoop(self) -> None:
    self.main.display.window.fill("#FFF8F0")
    self.main.display.ui = []

    start = self.main.display.addElement((200, 100), (50, 25), "#23CE6B")
    
    @start.bindOnClick
    def playEv():
      self.main.mode = "game"
      self.main.isInstRunning = False

    
    while self.main.isRunning and self.main.isInstRunning:
      
      self.main.display.render()
      self.main.eventHandle()
      self.main.clock.tick(self.main.tickrate)
      


# #FFF8F0, #01161E, #77878B, #23CE6B, #DD1C1A

#Error: play button doesn't work