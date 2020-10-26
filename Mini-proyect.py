import random 
board={"1": " ", "2": " ", "3": " ", "4": " ", "5": " ", "6": " ", "7": " ", "8": " ", "9": " "}
board_positions={"1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9"}
moves = 0

#Function show_board shows the two boards of the game, one with the numbers of the positions and other where the player and the computer will play.
def show_board(board, board_positions):
    print(board["1"] + "|" + board["2"] + "|" + board["3"])
    print("-----")
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print("-----")
    print(board["7"] + "|" + board["8"] + "|" + board["9"])
    print("-------------------- Positions --------------------")
    print(board_positions["1"] + "|" + board_positions["2"] + "|" + board_positions["3"])
    print("-----")
    print(board_positions["4"] + "|" + board_positions["5"] + "|" + board_positions["6"])
    print("-----")
    print(board_positions["7"] + "|" + board_positions["8"] + "|" + board_positions["9"])

#Function player puts an X in the position the player chooses.
#Parameter: move_player -> the position the player chooses.
def player(move_player):
    board[move_player] = "X"   

#Function computer puts an O in the position the computer chooses randomly between 1 and 9.
#Parameter: move_computer -> the position the computer chooses.
def computer(move_computer):
    board[move_computer]= "O"

#Function valid returns True if the position chosen is not occupied and False if the position is occupied.
#Parameter: move -> the position chosen by both the computer and the player.
def valid(move):
    if move=="1" or move=="2" or move=="3" or move=="4" or move=="5" or move=="6" or move=="7" or move=="8" or move=="9":  
        if board[move] == " ":
            return True
        else:
            return False
    else:
        return False

#Function win_player looks if the condition to win the game is met, if there are three X in a row.
def win_player(board):
    win = False
    if board["1"] == "X" and  board["2"] == "X" and board["3"] == "X":
        win = True
    elif board["4"] == "X" and  board["5"] == "X" and board["6"] == "X":
        win = True
    elif board["7"] == "X" and  board["8"] == "X" and board["9"] == "X":
        win = True
    elif board["1"] == "X" and  board["4"] == "X" and board["7"] == "X":
        win = True
    elif board["2"] == "X" and  board["5"] == "X" and board["8"] == "X":
        win = True
    elif board["3"] == "X" and  board["6"] == "X" and board["9"] == "X":
        win = True
    elif board["1"] == "X" and  board["5"] == "X" and board["9"] == "X":
        win = True
    elif board["3"] == "X" and  board["5"] == "X" and board["7"] == "X":
        win = True

    return win

#Function win_computer looks if the condition to win the game is met, if there are three O in a row.
def win_computer(board):
    win = False
    if board["1"] == "O" and  board["2"] == "O" and board["3"] == "O":
        win = True
    elif board["4"] == "O" and  board["5"] == "O" and board["6"] == "O":
        win = True
    elif board["7"] == "O" and  board["8"] == "O" and board["9"] == "O":
        win = True
    elif board["1"] == "O" and  board["4"] == "O" and board["7"] == "O":
        win = True
    elif board["2"] == "O" and  board["5"] == "O" and board["8"] == "O":
        win = True
    elif board["3"] == "O" and  board["6"] == "O" and board["9"] == "O":
        win = True
    elif board["1"] == "O" and  board["5"] == "O" and board["9"] == "O":
        win = True
    elif board["3"] == "O" and  board["5"] == "O" and board["7"] == "O":
        win = True

    return win

while True:
    show_board(board, board_positions)
    move_player=input("Choose a position in the board: ")
    #If the computer has not won and the moves are less than 9 the player chooses an option, if the option is not valid it keeps asking for an option
    if(win_computer(board) == False and moves<=9):
        while(valid(move_player) == False):
            move_player=input("That position is not valid, choose another position in the board: ")
        player(move_player)
        moves+=1
    #If the player has not won and the moves are less than 9 the computer chooses an option, if the option is not valid it keeps giving numbers until is valid
    move_computer= str(random.randint(1,9))
    if(win_player(board) == False and moves<=9):
        while(valid(move_computer) == False):
            move_computer= str(random.randint(1,9))
        computer(move_computer)
        moves+=1
    #The computer wins
    if win_computer(board) == True:
        print("The computer wins!")
        show_board(board, board_positions)
        break
    #The player wins    
    elif win_player(board) == True:
        print("You win!")
        show_board(board, board_positions)
        break
    #There is a tie        
    elif win_player(board) == False and win_computer(board) == False and moves == 9:
        print("It's a tie!")
        show_board(board, board_positions)
        break

