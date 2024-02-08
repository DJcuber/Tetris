class Leaderboard:
    def __init__(self, main):
        self.main = main
        self.leaderboardLoop()

    def leaderboardLoop(self):
        self.main.isModeRunning = True
        display = self.main.display
        display.window.fill("#FFF8F0")
        display.ui = []
    
        banner = display.addElement((0, 0), (display.windowSize[0], display.windowSize[1]*(1/4)), "#77878B", text="Leaderboard")
        
