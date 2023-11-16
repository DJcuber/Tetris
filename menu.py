import pygame as pg
import ui

class Menu:
  def __init__(self, main) -> None:
    self.main = main
    self.menuRunning = True
    self.menuLoop()

  def menuLoop(self) -> None:
    display = self.main.display
    display.window.fill("#FFF8F0")
    display.ui = []

    start = display.addElement((500, 500), (100, 100), "#23CE6B", text="play")
    
    @start.bindOnClick
    def playEv():
      self.main.mode = "game"
      self.main.isInstRunning = False

    banner = display.addElement((0, 0), (display.windowSize[0], display.windowSize[1]*(2/9)), "#77878B")

    
    while self.main.isRunning and self.main.isInstRunning:
      
      self.main.display.render()
      self.main.eventHandle()
      self.main.clock.tick(self.main.tickrate)
      


# #FFF8F0, #01161E, #77878B, #23CE6B, #DD1C1A
