from tkinter import *
from tkinter import messagebox
import random

window = Tk()
window.title('Tic-Tac-Toe')
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
player = 'O'
computer = 'X'


def positionIsFree(position):
    if board[position - 1] == "-":
        return True
    else:
        return False


def insertInPosition(letter, position):
    if positionIsFree(position):
        board[position - 1] = letter
        DrawonButton(letter, position)
        if checkDraw():
            messagebox.showinfo("Tic Tac Toe", "That's Draw")
            exit()
        if checkPossibleWins():
            if letter == 'X':
                messagebox.showerror("Tic Tac Toe", "Computer won")
                exit()
            else:
                messagebox.showerror("Tic Tac Toe", "player won")
                exit()
    else:
        messagebox.showerror("Tic Tac Toe", "Invalid position")


def checkPossibleWins():
    if (board[0] == board[1] == board[2] and board[0] != "-"):
        return True
    elif (board[3] == board[4] == board[5] and board[3] != "-"):
        return True
    elif (board[6] == board[7] == board[8] and board[6] != "-"):
        return True
    elif (board[0] == board[3] == board[6] and board[0] != "-"):
        return True
    elif (board[1] == board[4] == board[7] and board[1] != "-"):
        return True
    elif (board[2] == board[5] == board[8] and board[2] != "-"):
        return True
    elif (board[0] == board[4] == board[8] and board[0] != "-"):
        return True
    elif (board[2] == board[4] == board[6] and board[2] != "-"):
        return True


def checkWhichMarkWon(mark):
    winner = ""
    if (board[0] == board[1] == board[2] and board[0] != "-"):
        winner = board[0]
    elif (board[3] == board[4] == board[5] and board[3] != "-"):
        winner = board[3]
    elif (board[6] == board[7] == board[8] and board[6] != "-"):
        winner = board[6]
    elif (board[0] == board[3] == board[6] and board[0] != "-"):
        winner = board[0]
    elif (board[1] == board[4] == board[7] and board[1] != "-"):
        winner = board[1]
    elif (board[2] == board[5] == board[8] and board[2] != "-"):
        winner = board[2]
    elif (board[0] == board[4] == board[8] and board[0] != "-"):
        winner = board[0]
    elif (board[2] == board[4] == board[6] and board[2] != "-"):
        winner = board[2]
    if winner == mark:
        return True
    else:
        return False


def checkDraw():
    if (checkPossibleWins() == False):
        return True
    else:
        return False


def computerMove():
    bestScore = -1000
    bestMove = -100
    for i in range(9):
        if (board[i] == "-"):
            board[i] = computer
            score = miniMax(board, False)
            board[i] = ("-")
            if (score > bestScore):
                bestScore = score
                bestMove = i + 1

    insertInPosition(computer, bestMove)


def miniMax(board, isMaximizing):
    if (checkWhichMarkWon(computer)):
        return 1
    elif (checkWhichMarkWon(player)):
        return -1
    elif (checkDraw()):
        return 0

    if (isMaximizing):
        bestScore = -800
        for i in range(9):
            if (board[i] == "-"):
                board[i] = computer
                score = miniMax(board, False)
                board[i] = "-"
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        for i in range(9):
            if (board[i] == "-"):
                board[i] = player
                score = miniMax(board, True)
                board[i] = "-"
                if (score < bestScore):
                    bestScore = score

        return bestScore


def PTB(position):
    if (position == 1):
        b = b1
    elif (position == 2):
        b = b2
    elif (position == 3):
        b = b3
    elif (position == 4):
        b = b4
    elif (position == 5):
        b = b5
    elif (position == 6):
        b = b6
    elif (position == 7):
        b = b7
    elif (position == 8):
        b = b8
    elif (position == 9):
        b = b9
    return b


def BTP(b):
    if (b == b1):
        position = 1
    elif (b == b2):
        position = 2
    elif (b == b3):
        position = 3
    elif (b == b4):
        position = 4
    elif (b == b5):
        position = 5
    elif (b == b6):
        position = 6
    elif (b == b7):
        position = 7
    elif (b == b8):
        position = 8
    elif (b == b9):
        position = 9
    return position


def DrawonButton(letter, position):
    b = PTB(position)
    b.configure(text=letter, bg='blue', fg='white')
    board[position - 1] = letter


def clickb(b):
    position = BTP(b)
    insertInPosition(player, position)
    computerMove()


b1 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: clickb(b1))
b2 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: clickb(b2))
b3 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: clickb(b3))
b4 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: clickb(b4))
b5 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: clickb(b5))
b6 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: clickb(b6))
b7 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: clickb(b7))
b8 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: clickb(b8))
b9 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: clickb(b9))
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)
List1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
position = random.choice(List1)
insertInPosition("X", position)
window.mainloop()
