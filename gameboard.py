from tkinter import *
from tkinter import messagebox, simpledialog


class Game:
    def __init__(self, pc, mv):
        self.user_name = self.getName()
        self.other_player = ""
        self.player_char = pc  # next_player to move
        self.turn = mv
        self.games_played = 0
        self.ties_count = 0
        self.wins = 0
        self.loss_count = 0
        self.last_player = ""
        self.root = Tk()  # Window defined
        self.root.title("Tic-Tac-Toe")  # Title given
        self.colour = {'O': "deep sky blue", 'X': "lawn green"}
        self.b = [[], [], []]
        for i in range(3):
            for j in range(3):
                self.b[i].append(self.button(self.root))
                self.b[i][j].config(command=lambda row=i, col=j: self.click(row, col))
                self.b[i][j].grid(row=i, column=j)
        self.label = Label(text=self.user_name + "'s Chance", font=('arial', 20, 'bold'))
        self.label.grid(row=3, column=0, columnspan=3)
        self.close = Button(self.root, text="Quit", command=self.close_window, font=('arial', 20, 'bold'), bg="Blue")
        self.close.grid(row=4, column=0, columnspan=3)
        self.stats = Label(self.root, text="Statistics", font=('arial', 20, 'bold'))
        self.stats.grid(row=0, column=3, rowspan=4, columnspan=4)

    def getName(self):
        popup = Tk()
        lb = Label(popup, text="Enter Name: ")
        ip = Entry(popup)
        name = ""
        lb.pack()
        ip.pack()

        def submitName():
            nonlocal name
            name = ip.get()
            popup.destroy()

        sb = Button(popup, text="submit", command=submitName)
        sb.pack()
        popup.mainloop()
        return name

    @staticmethod
    def button(frame):  # Function to define a button
        b = Button(frame, padx=1, bg="papaya whip", width=3, text="   ", font=('arial', 60, 'bold'), relief="sunken",
                   bd=10)
        return b

    def updateGamesPlayed(self, res):
        self.games_played += 1
        if res == "win":
            self.wins += 1
        elif res == "loss":
            self.loss_count += 1
        elif res == "draw":
            self.ties_count += 1

    def resetGameBoard(self):  # Resets the game
        for i in range(3):
            for j in range(3):
                self.b[i][j]["text"] = ""
                self.b[i][j]["state"] = NORMAL
        self.turn = self.turn

    def isWinner(self):
        # horizontal
        rows = [0] * 3
        cols = [0] * 3
        for i in range(3):
            for j in range(3):
                if self.b[i][j]["text"] == self.player_char:
                    rows[i] += 1
                    cols[j] += 1
        if max(rows + cols) == 3:
            return True
        ldiag = 0
        rdiag = 0
        for i in range(3):
            if self.b[i][i]["text"] == self.player_char:
                ldiag += 1
            if self.b[i][3 - 1 - i]["text"] == self.player_char:
                rdiag += 1
        return max(ldiag, rdiag) >= 3

    def enableAll(self):
        for i in range(3):
            for j in range(3):
                if self.b[i][j]["text"] == "":
                    self.b[i][j]["state"] = NORMAL

    def disableAll(self):
        for i in range(3):
            for j in range(3):
                self.b[i][j]["state"] = DISABLED

    def boardIsFull(self):
        cnt = 0
        for i in range(3):
            for j in range(3):
                if self.b[i][j]["text"] == '':
                    cnt += 1
        return cnt == 9

    def printStatus(self):
        text="Statistics\n"
        text += f"Name: {self.user_name}\n Last Player: {self.last_player}\n"
        text += f"Number of games played: {self.games_played}\nWins: {self.wins}\n"
        text += f"Number of ties: {self.ties_count}\nNumber of losses: {self.loss_count}"

    def click(self, row, col):
        self.b[row][col].config(text=self.player_char, state=DISABLED, disabledforeground=self.colour[self.player_char])
        self.label.config(text=self.user_name + "'s Chance")

    def close_window(self):
        self.root.destroy()

    def play(self):
        self.root.mainloop()


if __name__ == "__main__":
    cc = Game("X", True)
    cc.play()
