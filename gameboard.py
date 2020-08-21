from tkinter import *
from tkinter import messagebox


class Game:
    def __init__(self):
        self.user_name = self.getName()
        self.player = 'X'  # next_player to move
        self.games_played = 0
        self.ties_count = 0
        self.wins = 0
        self.loss_count = 0

        self.root = Tk()  # Window defined
        self.root.title("Tic-Tac-Toe")  # Title given
        self.colour = {'O': "deep sky blue", 'X': "lawn green"}
        self.b = [[], [], []]
        for i in range(3):
            for j in range(3):
                self.b[i].append(self.button(self.root))
                self.b[i][j].config(command=lambda row=i, col=j: self.click(row, col))
                self.b[i][j].grid(row=i, column=j)
        self.label = Label(text=self.player + "'s Chance", font=('arial', 20, 'bold'))
        self.label.grid(row=3, column=0, columnspan=3)
        self.close = Button(self.root, text="Quit", command=self.close_window, font=('arial', 20, 'bold'), bg="Blue")
        self.close.grid(row=4, column=0, columnspan=3)

    def getName(self):
        name = input("Enter Name: ")
        return name

    @staticmethod
    def button(frame):  # Function to define a button
        b = Button(frame, padx=1, bg="papaya whip", width=3, text="   ", font=('arial', 60, 'bold'), relief="sunken",
                   bd=10)
        return b

    def change_a(self):  # Function to change the operand for the next player
        for i in ['O', 'X']:
            if not (i == self.player):
                self.player = i
                break

    def updateGamesPlayed(self):
        # TODO
        pass

    def resetGameBoard(self):  # Resets the game
        for i in range(3):
            for j in range(3):
                self.b[i][j]["text"] = " "
                self.b[i][j]["state"] = NORMAL
        self.player = 'X'

    def isWinner(self):
        # TODO
        pass

    def enableAll(self):
        # TODO
        pass

    def disableAll(self):
        # TODO
        pass

    def boardIsFull(self):
        # TODO
        pass

    def printStatus(self):
        # TODO
        pass

    def click(self, row, col):
        self.b[row][col].config(text=self.player, state=DISABLED, disabledforeground=self.colour[self.player])

        self.change_a()
        self.label.config(text=self.player + "'s Chance")

    def close_window(self):
        self.root.destroy()



    def play(self):
        self.root.mainloop()


if __name__ == "__main__":
    cc = Game()
    cc.play()
