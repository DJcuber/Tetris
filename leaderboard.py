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
        for i, record in enumerate(data):
            scoreList[i] = Score(record[0], record[1], record[2])
        self.insertionSort(scoreList)
        for i in scoreList:
            print(i.score)
    
        banner = display.addElement((0, 0), (display.windowSize[0], display.windowSize[1]*(1/4)), "#77878B", text="Leaderboard")
        background = display.addElement((display.windowSize[0]*2/7, display.windowSize[1]*3/10), (display.windowSize[0]*3/7, display.windowSize[1]*13/20), "#D3D3D3")

        while self.main.isRunning and self.main.isModeRunning:
          self.main.display.render()
          if self.main.eventHandle():
            return 1
          self.main.clock.tick(self.main.tickrate)

    def insertionSort(self, scores):
        for i in range(1, len(scores)):
            index = i
            value = scores[i]
            while index > 0 and scores[index-1].score < value.score:
                scores[index] = scores[index-1]
                index -= 1
            scores[index] = value

class Score:
    def __init__(self, playerID, date, score):
        self.playerID = playerID
        self.date = date
        self.score = score


