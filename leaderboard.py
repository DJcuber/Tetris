class Leaderboard:
    def __init__(self, main):
        self.main = main
        self.leaderboardLoop()

    def leaderboardLoop(self):
        self.main.isModeRunning = True
        display = self.main.display
        display.window.fill("#FFF8F0")
        display.ui = []

        self.main.cursor.execute("SELECT userName, datePlayed, score FROM score, player WHERE score.playerID = player.playerID")
        data = self.main.cursor.fetchall()
        scoreList = [None]*len(data)
        for i, record in enumerate(data):
            scoreList[i] = Score(record[0], record[1], record[2])
        self.insertionSort(scoreList)
    
        banner = display.addElement((0, 0), (display.windowSize[0], display.windowSize[1]*(1/4)), "#77878B", text="Leaderboard")
        background = display.addElement((display.windowSize[0]*2/7, display.windowSize[1]*7/20), (display.windowSize[0]*3/7, display.windowSize[1]*1/2), "#D3D3D3")

        scoresUI = []
        for i in range(10):
            if i < len(scoreList):
                entry = scoreList[i]
                scoresUI.append(display.addElement((display.windowSize[0]*2/7, display.windowSize[1]*(7+i)/20), (display.windowSize[0]*3/7, display.windowSize[1]/20), "#D3D3D3", text = f"{entry.name: <15} {entry.date: ^10} {entry.score: >15}"))
        
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
    def __init__(self, name, date, score):
        self.name = name
        self.date = str(date)
        self.score = score


