class Leaderboard:
    def __init__(self, main):
        self.main = main
        self.leaderboardLoop()

    def leaderboardLoop(self):
        self.main.isModeRunning = True
        display = self.main.display
        display.window.fill("#FFF8F0")
        display.ui = []

        self.main.cursor.execute("SELECT playerID, datePlayed, score FROM score")
        data = self.main.cursor.fetchall()
        scoreList = [None]*len(data)
        print(data)
        for i, record in enumerate(data):
            scoreList[i] = Score(record[0], record[1], record[2])
        print(scoreList[0].date)
    
        banner = display.addElement((0, 0), (display.windowSize[0], display.windowSize[1]*(1/4)), "#77878B", text="Leaderboard")

        while self.main.isRunning and self.main.isModeRunning:
          self.main.display.render()
          if self.main.eventHandle():
            return 1
          self.main.clock.tick(self.main.tickrate)

    def insertionSort(self, scores):
        

class Score:
    def __init__(self, playerID, date, score):
        self.playerID = playerID
        self.date = date
        self.score = score
