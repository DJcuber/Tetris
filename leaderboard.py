class Leaderboard:
    def __init__(self, main) -> None:
        self.main: object = main
        self.leaderboardLoop()

    def leaderboardLoop(self) -> int:
        display = self.main.display
        display.window.fill("#FFF8F0")
        display.ui = []

        data = self.main.db.search("SELECT userName, datePlayed, score FROM score, player WHERE score.playerID = player.playerID")
        
        scoreList = [None]*len(data)
        for i, record in enumerate(data):
            scoreList[i] = Score(record[0], record[1], record[2])
        self.insertionSort(scoreList)
    
        banner = display.addElement((0, 0), (display.windowSize[0], display.windowSize[1]*(1/4)), "#77878B", text="Leaderboard")
        background = display.addElement((display.windowSize[0]*2/7, display.windowSize[1]*7/20), (display.windowSize[0]*3/7, display.windowSize[1]*1/2), "#D3D3D3")
        menu = display.addElement((display.windowSize[0]/20, display.windowSize[1]/20), (display.windowSize[0]/20, display.windowSize[1]/20), "#DD1C1A", text = "<-")

        @menu.bindOnClick
        def menuEv():
            self.main.mode = "menu"
            self.main.isModeRunning = False
        
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

    def insertionSort(self, scores) -> None:
        for i in range(1, len(scores)):
            index = i
            value = scores[i]
            while index > 0 and scores[index-1].score < value.score:
                scores[index] = scores[index-1]
                index -= 1
            scores[index] = value

class Score:
    def __init__(self, name, date, score) -> None:
        self.name: str = name
        self.date: str = str(date)
        self.score: int = score


