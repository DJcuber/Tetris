import pygame as pg
import ui
import time

class GameOver:
    def __init__(self, main, score):
        self.main = main
        self.score = score
        self.gameOverLoop()

    def gameOverLoop(self):
        self.main.isModeRunning = True
        display = self.main.display
        display.window.fill("#FFF8F0")
        display.ui = []
    
        banner = display.addElement((0, 0), (display.windowSize[0], display.windowSize[1]*(1/4)), "#77878B", text="Game Over")

        score = display.addElement((display.windowSize[0]*4/11, display.windowSize[1]*3/10), (display.windowSize[0]*3/11, display.windowSize[1]//10), "#FFF8F0", text = f"score: {self.score}")

        playAgain = display.addElement((display.windowSize[0]*4/11, display.windowSize[1]*3/5), (display.windowSize[0]*3/11, display.windowSize[1]//10), "#23CE6B", text = "Play Again")

        menu = display.addElement((display.windowSize[0]*4/11, display.windowSize[1]*3/4), (display.windowSize[0]*3/11, display.windowSize[1]//10), "#D3D3D3", text = "Menu")

        @playAgain.bindOnClick
        def playAgainEv():
            self.main.mode = "game"
            self.main.isModeRunning = False

        @menu.bindOnClick
        def menuEv():
            self.main.mode = "menu"
            self.main.isModeRunning = False

        currentDate = time.strftime("%Y-%m-%d", time.gmtime())
        
        self.main.cursor.execute(f'INSERT INTO score(score, datePlayed, playerID) VALUES({self.score}, "{currentDate}", {self.main.user})')

        
        while self.main.isRunning and self.main.isModeRunning:
          self.main.display.render()
          if self.main.eventHandle():
            return 1
          self.main.clock.tick(self.main.tickrate)

"""
from time import gmtime, strftime
strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
'Thu, 28 Jun 2001 14:17:15 +0000'
"""
