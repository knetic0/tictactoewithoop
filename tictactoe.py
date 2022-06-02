from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askyesno

class Main:
    def __init__(self):
        self.window = Tk()
        self.window.title("TicTacToe")
        self.window.resizable(False, False)
        self.window.geometry("225x275")

        self.list = []
        self._control = True
        self.timer = 0

        self.winnerCanvas = Canvas(self.window, bg = "black")
        self.winnerCanvas.place(x = 0, y = 0, width = self.window.winfo_screenwidth(), height = 50)
        self.textArea = self.winnerCanvas.create_text(125, 25, text="Welcome!", fill = "white", font = "ubuntu, 16")

        Main.createButtons(self)

        self.window.mainloop()

    def buttons(self, xCor, yCor, index):
        self.xCor = xCor
        self.yCor = yCor
        self.allButtons = Button(self.window, bg = "white", command= lambda: Main.gamePlay(self, index))
        self.allButtons.place(x = self.xCor, y = self.yCor, height = 75, width = 75)
        self.list.append(self.allButtons)

    def createButtons(self):
        self.x = 0
        self.y = 0
        for i in range(9):
            if i < 3:
                Main.buttons(self, self.x + (i * 75), self.y + 50, i)
            elif 3 <= i < 6:
                Main.buttons(self, self.x + ((i - 3) * 75), self.y + 125, i)
            else:
                Main.buttons(self, self.x + ((i - 6) * 75), self.y + 200, i)
        
    def gamePlay(self, index):
        if self._control == True:
            self.buttonControl = "X"
            self.list[index].config(text = self.buttonControl, state = DISABLED)
            self.winnerCanvas.itemconfig(self.textArea, text = "O Turn")
            self._control = False
        else:
            self.buttonControl = "O"
            self.list[index].config(text = self.buttonControl, state = DISABLED)
            self.winnerCanvas.itemconfig(self.textArea, text = "X Turn")
            self._control = True
        
        Main.checkWinner(self)
    
    def changeWinner(self, first, second, third):
        self.list[first].config(bg = "green")
        self.list[second].config(bg = "green")
        self.list[third].config(bg = "green")
        self.winnerCanvas.itemconfig(self.textArea, text = f"{self.buttonControl} Winner")
        self.yesno = askyesno("TicTacToe", "Do you wanna play again?")
        if self.yesno:
            Main.restart(self)
        else:
            self.window.destroy()

    def checkWinner(self):
        self.timer += 1
        if (self.list[0]["text"] == self.buttonControl and self.list[1]["text"] == self.buttonControl and self.list[2]["text"] == self.buttonControl):
            Main.changeWinner(self, 0, 1, 2)
        elif (self.list[0]["text"] == self.buttonControl and self.list[3]["text"] == self.buttonControl and self.list[6]["text"] == self.buttonControl):
            Main.changeWinner(self, 0, 3, 6)
        elif (self.list[3]["text"] == self.buttonControl and self.list[4]["text"] == self.buttonControl and self.list[5]["text"] == self.buttonControl):
            Main.changeWinner(self, 3, 4, 5)
        elif (self.list[6]["text"] == self.buttonControl and self.list[7]["text"] == self.buttonControl and self.list[8]["text"] == self.buttonControl):
            Main.changeWinner(self, 6, 7, 8)
        elif (self.list[1]["text"] == self.buttonControl and self.list[4]["text"] == self.buttonControl and self.list[7]["text"] == self.buttonControl):
            Main.changeWinner(self, 1, 4, 7)
        elif (self.list[2]["text"] == self.buttonControl and self.list[5]["text"] == self.buttonControl and self.list[8]["text"] == self.buttonControl):
            Main.changeWinner(self, 2, 5, 8)
        elif (self.list[0]["text"] == self.buttonControl and self.list[4]["text"] == self.buttonControl and self.list[8]["text"] == self.buttonControl):
            Main.changeWinner(self, 0, 4, 8)
        elif (self.list[2]["text"] == self.buttonControl and self.list[4]["text"] == self.buttonControl and self.list[6]["text"] == self.buttonControl):
            Main.changeWinner(self, 2, 4, 6)
        elif self.timer == 9:
            self.winnerCanvas.itemconfig(self.textArea, text = "Tie")
            self.tieQue = askyesno("Tie!", "Do you wanna play again?")
            if self.tieQue:
                Main.restart(self)
            else:
                self.window.destroy()

    def restart(self):
        self.winnerCanvas.itemconfig(self.textArea, text = "Welcome Again")
        self._control = True
        self.timer = 0
        self.buttonControl = "X"
        self.winnerCanvas.itemconfig(self.textArea, text = "X Turn")
        for i in range(len(self.list)):
            self.list[i].config(text = " ", bg = "white", state = NORMAL)

if __name__ == "__main__":
    Main()