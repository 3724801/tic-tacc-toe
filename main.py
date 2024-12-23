board=["-", "-", "-",
       "-", "-", "-",
       "-", "-", "-"]

player = 'O'
computer = 'X'

def printtable(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

printtable(board)

def positionIsFree(position):
  if board[position]=="-":   
    return True
  else:
    return False

def insertInPosition(letter, position):
    if positionIsFree(position):
        board[position] = letter
        printtable(board)

        if checkDraw():
            print(checkDraw())
            print("Draw!!")
            exit()
        if checkPossibleWins():
            if letter == 'X':
                print("Bot wins!")
                exit()
            else:
                print("Hoooraaay!!!, Player wins")
                exit()
        return

    else:
        print("Invalid position")
        position = int(input("Enter a new position: "))
        insertInPosition(letter, position)
        return


def checkPossibleWins():
  if  (board[0] == board[1] and board[1]==board[2] and board[0] != '-'):
    return True
  elif(board[3] == board[4] and board[4]==board[5] and board[3] != '-'):
    return True
  elif(board[6] == board[7] and board[7]==board[8] and board[6] != '-'):
    return True
  elif(board[0] == board[3] and board[3]==board[6] and board[0] != '-'):
    return True
  elif(board[1] == board[4] and board[1]==board[7] and board[1] != '-'):
    return True
  elif(board[2] == board[5] and board[2]==board[8] and board[2] != '-'):
    return True
  elif(board[0] == board[4] and board[0]==board[8] and board[0] != '-'):
    return True
  elif(board[2] == board[4] and board[2]==board[6] and board[2] != '-'):
    return True
  else:
    return False

def checkWhichMarkWon(mark):     
  if  (board[0] == board[1] and board[1]==board[2] and board[0] == mark):
    return True
  elif(board[3] == board[4] and board[4]==board[5] and board[3] == mark):
    return True
  elif(board[6] == board[7] and board[7]==board[8] and board[6] == mark):
    return True
  elif(board[0] == board[3] and board[3]==board[6] and board[0] == mark):
    return True
  elif(board[1] == board[4] and board[1]==board[7] and board[1] == mark):
    return True
  elif(board[2] == board[5] and board[2]==board[8] and board[2] == mark):
    return True
  elif(board[0] == board[4] and board[0]==board[8] and board[0] == mark):
    return True
  elif(board[2] == board[4] and board[2]==board[6] and board[2] == mark):
    return True
  else:
    return False

def checkDraw():
  for i in range(9):
    if (board[i] == "-"):
        return True
    return False

def playerMove():
    run=True
    while run :
        move = int(input("Please select position for 'x'(1-9)"))
        if move>0 and move<10:
            if positionIsFree(move-1):
                run = False
                insertInPosition("O", move-1) 
            else:
                print("Sorry this space is occupied")
        else:
            print("Please type the number within the range")

def computerMove():
  bestScore=-1000
  bestMove=-100
  for i in range(9):
      if (positionIsFree(i)):
        board[i]=computer
        score=miniMax(board,False)
        board[i]=("-")
        if(score>bestScore):
          bestScore=score
          bestMove=i
  insertInPosition('X',bestMove)
  return 0

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
            if (positionIsFree(i)):
                board[i] = player
                score = miniMax(board, True)
                board[i] = "-"
                if (score < bestScore):
                    bestScore = score
        return bestScore

while not checkPossibleWins():
	computerMove()
	playerMove()