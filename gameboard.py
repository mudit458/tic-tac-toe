from tkinter import *
from tkinter import messagebox


class Game:
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

    def reset(self):  # Resets the game
        for i in range(3):
            for j in range(3):
                self.b[i][j]["text"] = " "
                self.b[i][j]["state"] = NORMAL
        self.player = 'X'

    def check(self):  # Checks for victory or Draw
        for i in range(3):
            if (self.b[i][0]["text"] == self.b[i][1]["text"] == self.b[i][2]["text"] == self.player or self.b[0][i][
                "text"] == self.b[1][i]["text"] ==
                    self.b[2][i][
                        "text"] == self.player):
                return self.player
        if (self.b[0][0]["text"] == self.b[1][1]["text"] == self.b[2][2]["text"] == self.player or self.b[0][2][
            "text"] ==
                self.b[1][1]["text"] == self.b[2][0][
                    "text"] == self.player):
            return self.player
        elif (self.b[0][0]["state"] == self.b[0][1]["state"] == self.b[0][2]["state"] == self.b[1][0]["state"] ==
              self.b[1][1]["state"] ==
              self.b[1][2][
                  "state"] == self.b[2][0]["state"] == self.b[2][1]["state"] == self.b[2][2]["state"] == DISABLED):
            return "draw"
        return None

    def click(self, row, col):
        self.b[row][col].config(text=self.player, state=DISABLED, disabledforeground=self.colour[self.player])
        # TODO WIN/LOSE
        ck = self.check()
        if ck is not None:
            yes = messagebox.askyesno("Rematch", "Do you want to play again?")
            if yes:
                self.reset()
                self.play()
            # TODO
            # show_stats()

        self.change_a()
        self.label.config(text=self.player + "'s Chance")

    def close_window(self):
        self.root.destroy()

    def __init__(self):
        self.root = Tk()  # Window defined
        self.root.title("Tic-Tac-Toe")  # Title given
        self.player = 'X'  # Two operators defined
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

    def play(self):
        self.root.mainloop()


if __name__ == "__main__":
    cc = Game()
    cc.play()
