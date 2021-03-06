import threading
from random import random
from tkinter import *
from tkinter import messagebox


def promptInput(message):
    res = ""

    win = Tk()
    label = Label(win, text=message)
    ipbox = Entry(win)

    def submit():
        nonlocal res
        res = ipbox.get()
        if res.strip() != "":
            win.destroy()

    button = Button(win, text="Submit", command=submit)
    label.pack()
    ipbox.pack()
    button.pack()
    win.mainloop()
    return res


class Game:
    def __init__(self, pc):
        self.con = ""
        self.user_name = ""
        while self.user_name == "":
            self.user_name = promptInput("Enter Username")
            # self.user_name = "abc"
        self.myTurn = False
        self.xy = ""
        self.other_player = ""
        self.player_char = pc  # X/O
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
                self.b[i][j].config(text="", command=lambda row=i, col=j: self.click(row, col))
                self.b[i][j].grid(row=i, column=j)
        self.label = Label(text="Chance", font=('arial', 20, 'bold'))
        self.label.grid(row=3, column=0, columnspan=3)
        self.close = Button(self.root, text="Quit", command=self.close_window, font=('arial', 20, 'bold'), bg="Blue")
        self.close.grid(row=4, column=0, columnspan=3)
        self.stats = Label(self.root, text="Statistics", font=('arial', 20, 'bold'))
        self.stats.grid(row=0, column=3, rowspan=4, columnspan=4)

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
        elif res == "tie":
            self.ties_count += 1

    def resetGameBoard(self):  # Resets the game
        for i in range(3):
            for j in range(3):
                self.b[i][j]["text"] = ""
                self.b[i][j]["state"] = NORMAL
        self.last_player = ""
        self.printStatus()

    def isWinner(self):
        # horizontal
        for char in ("X", "O"):
            rows = [0] * 3
            cols = [0] * 3
            for i in range(3):
                for j in range(3):
                    if self.b[i][j]["text"] == char:
                        rows[i] += 1
                        cols[j] += 1
            if max(rows + cols) == 3:
                return char
            ldiag = 0
            rdiag = 0
            for i in range(3):
                if self.b[i][i]["text"] == char:
                    ldiag += 1
                if self.b[i][3 - 1 - i]["text"] == char:
                    rdiag += 1
            if max(ldiag, rdiag) >= 3:
                return char
        return None

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
                if self.b[i][j]["text"] in ('X', 'O'):
                    cnt += 1
        if cnt == 9:
            return True
        return False

    def printStatus(self):
        text = "Statistics\n"
        text += f"Name: {self.user_name}\n Last Player: {self.last_player}\n"
        text += f"Number of games played: {self.games_played}\nWins: {self.wins}\n"
        text += f"Number of ties: {self.ties_count}\nNumber of losses: {self.loss_count}"
        self.stats["text"] = text
        self.root.update()

    def play_again(self):
        self.root.withdraw()
        yes = messagebox.askyesno("Again?", "Do you want to play again???")
        print(yes)
        print('out of loop')

        if self.myTurn:
            if yes:
                self.con.send("Play Again".encode('utf-8'))
            else:
                self.con.send("Fun Times")
            response = self.con.recv(2048).decode('utf-8')
        else:
            response = self.con.recv(2048).decode('utf-8')
            if yes:
                self.con.send("Play Again".encode('utf-8'))
            else:
                self.con.send("Fun Times".encode('utf-8'))
        if yes and response == 'Play Again':
            self.resetGameBoard()
        else:
            for i in range(3):
                for j in range(3):
                    self.b[i][j].config(text="*", state=DISABLED, bg='grey', disabledforeground='red')
            self.label["text"] = "Not in play"
            self.root.update()
        self.root.deiconify()

    def click(self, row=-1, col=-1):
        self.xy = str(row) + " " + str(col)
        self.disableAll()
        if self.myTurn:
            self.b[row][col].config(state=DISABLED, disabledforeground=self.colour[self.player_char])
            self.b[row][col].config(text=self.player_char)
            self.root.update()
            self.con.send(f"{row} {col}".encode('utf-8'))
            print("sent ", row, col)
        else:
            print("waiting for move")
            if self.player_char == "X":
                other = "O"
            else:
                other = "X"
            # get other player's move
            print("waiting for other player to make a move")
            xy = self.con.recv(2048).decode('utf-8')
            if xy == "quit":
                print("other Player Quit")
                self.root.destroy()
                sys.exit()
            print("other player moved at", xy)
            row, col = map(int, xy.split())
            self.b[row][col].config(text=other)
            self.b[row][col].config(state=DISABLED, disabledforeground=self.colour[other])
        # check win
        res = self.isWinner()
        if res:
            if res == self.player_char:
                winner = self.user_name
                self.updateGamesPlayed('win')
            else:
                winner = self.other_player
                self.updateGamesPlayed('loss')
            self.printStatus()
            self.play_again()

            return

        # check draw
        res = self.boardIsFull()
        if res:
            messagebox.Message("The game resulted in a draw")
            self.updateGamesPlayed('tie')
            messagebox.Message(message="The game tied")
            self.printStatus()
            self.resetGameBoard()
            self.printStatus()
            self.play_again()
            return

        self.myTurn = not self.myTurn

        if self.myTurn:
            self.label.config(text=f"{self.user_name}' Turn")
            self.last_player = self.other_player
        else:
            self.label.config(text=f"{self.other_player}'s Turn")
            self.last_player = self.user_name
        self.printStatus()
        self.root.update()

        if self.myTurn:
            self.enableAll()
        else:
            self.click()

    def close_window(self):
        if self.myTurn:
            self.con.send("quit".encode('utf-8'))
        self.root.destroy()

    def start_game_window(self):
        mainloop()

    def play(self):
        self.printStatus()
        if self.myTurn:
            self.label["text"] = f"{self.user_name}' Turn"
        else:
            self.label["text"] = f"{self.other_player}'s Turn"
        self.start_game_window()
