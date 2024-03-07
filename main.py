from tkinter import *
import random

def nextTurn(row, column):
    global player

    if buttons[row][column]['text'] == "" and checkWinner() is False:

        if player == players[0]: # We use this instead so we can use different symbols late

            buttons[row][column]['text'] = player

            if checkWinner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))

            elif checkWinner() is True:
                label.config(text=(players[0]+" wins"))

            elif checkWinner() == "Tie":
                label.config(text="Tie!")

        else:

            buttons[row][column]['text'] = player

            if checkWinner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))

            elif checkWinner() is True:
                label.config(text=(players[1]+" wins"))

            elif checkWinner() == "Tie":
                label.config(text="tie!")


def checkWinner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "": # horizontal Win conditions
            return True

    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "": # vertical Win conditions
            return True

    if buttons[0][0]["text"] == buttons[1][2]["text"] == buttons[2][2]["text"] != "": # diagonal win conditions
        return True

    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    elif checkEmptySpaces() is False:
        return "Tie"

    else:
        return False

def checkEmptySpaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -= 1
            
    if spaces == 0:
        return False
    else:
        return True

def restart():
    global player

    player = random.choice(players)
    label.config(text=(player + " turn"))
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="")

window = Tk()
window.title("Tik Tac Toe")
players = ["x", "0"]
player = random.choice(players)

buttons = [
    [0, 0, 0],
    [0, 0, 0], 
    [0, 0, 0]] # 2D list

label = Label(text= player + " turn", font=("sans-serif", 40))
label.pack(side="top")
reset_button = Button(text="restart", font=("sans-serif", 20), command=restart)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

# Now to add a button to each "0" we can use a nested for loop
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=("sans-serif", 40), width=5, height=2, command=lambda row=row, column=column: nextTurn(row, column)) 
        buttons[row][column].grid(row=row, column=column)

window.mainloop()