import pygame as pg
import ui

class Menu:
  def __init__(self, main) -> None:
    self.main = main
    self.menuLoop()

  def menuLoop(self) -> None:
    display = self.main.display
    display.window.fill("#FFF8F0")
    display.ui = []

    banner = display.addElement((0, 0), (display.windowSize[0], display.windowSize[1]*(1/4)), "#77878B", text="Tetrin Time")

    play = display.addElement((display.windowSize[0]*4/11, display.windowSize[1]*3/10), (display.windowSize[0]*3/11, display.windowSize[1]//10), "#23CE6B", text="Play")


    leaderboard = display.addElement((display.windowSize[0]*4/11, display.windowSize[1]*9/20), (display.windowSize[0]*3/11, display.windowSize[1]//10), "#D3D3D3", text="Leaderboard")

    exit = display.addElement((display.windowSize[0]*4/11, display.windowSize[1]*3/4), (display.windowSize[0]*3/11, display.windowSize[1]//10), "#DD1C1A", text="Quit")
    
    @play.bindOnClick
    def playEv():
      self.main.mode = "game"
      self.main.isModeRunning = False

    @leaderboard.bindOnClick
    def leaderboardEv():
      self.main.mode = "leaderboard"
      self.main.isModeRunning = False
    
    @exit.bindOnClick
    def exitEv():
      self.main.isRunning = False
      self.main.isModeRunning = False
      


    
    while self.main.isRunning and self.main.isModeRunning:
      
      self.main.display.render()
      if self.main.eventHandle():
        return 1
      self.main.clock.tick(self.main.tickrate)
      


# #FFF8F0, #01161E, #77878B, #23CE6B, #DD1C1A, #D3D3D3
