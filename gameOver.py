import pygame as pg
import ui

class GameOver:
    def __init__(self, main):
        self.main = main
        self.gameOverLoop()

    def gameOverLoop(self):
        display = self.main.display
        display.window.fill("#FFF8F0")
        display.ui = []
    
        #banner = display.addElement()
