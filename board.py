class board:

    slot = [[0]*3 for i in range(3)]
    turn: str = "x"

    def __init__(self):
        for i in range(0, 3):
            for j in range(0, 3):
                self.slot[j][i] = "-"

    def display(self):
        print("*****")
        for i in range(0, 3):
            print(self.slot[i][0] + " " + self.slot[i][1] + " " + self.slot[i][2])
        print("*****")

    def nextTurn(self):
        if self.turn == "x":
            self.turn = "o"
        else:
            self.turn = "x"

    def isWin(self):
        if self.rowCheck() or self.colCheck() or self.diagCheck():
            return 1
        else:
            return 0

    def isFull(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.slot[j][i] == "-":
                    return 0
        return 1

    def colCheck(self):
        for i in range(0, 3):
            if self.slot[i][0] == self.slot[i][1] and self.slot[i][1] == self.slot[i][2] and self.slot[i][0] != "-":
                return 1
        return 0

    def rowCheck(self):
        for i in range(0, 3):
            if self.slot[0][i] == self.slot[1][i] and self.slot[1][i] == self.slot[2][i] and self.slot[0][i] != "-":
                return 1
        return 0

    def diagCheck(self):
        if self.slot[0][0] == self.slot[1][1] and self.slot[1][1] == self.slot[2][2] and self.slot[0][0] != "-":
            return 1
        if self.slot[2][0] == self.slot[1][1] and self.slot[1][1] == self.slot[0][2] and self.slot[2][0] != "-":
            return 1
        return 0

    def place(self, col, row):
        col = col - 1
        row = row - 1
        if col < 0 or col > 2 or row > 2 or row < 0:
            print("Error, slot unavailable")
            return 0
        elif self.slot[col][row] == "-":
            self.slot[col][row] = self.turn
            return 1
        else:
            print("Error, slot unavailable")
            return 0
