#board
#display board

# play game
    #handles turn
#check win
    #check rows
    #check columns
    #check diagonals
#check tie

# flip player



# GLOBAL VARIABLE
game_still_going=True
#who won?or tie?
winner=None
#who's turn is it
current_player="X"
board=['-','-','-','-','-','-','-','-','-']

def display_board():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])

#play the game of tic tac toe
def play_game():
    
    #display the board initially
    display_board()

    #ehile the game is still going
    while game_still_going:
        #handle the single player turn of an arbitary player
        handle_turn(current_player)
        
        check_if_game_over()

        # flip the other player
        flip_player()
    
    #game has ended
    if winner=="X" or winner=="O":
        print(winner+" won. ")
    elif winner==None:
        print("Tie.")

#handle a single turn of an arbitary player
def handle_turn(player):
    print(player+"'s turn.")
    position=input("Choose a position from 1 to 9 : ")
    valid=False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position=input("Invalid input!! \n Choose a position from 1 to 9 : ")

        position=int(position)-1
        # print(position)
        if board[position]=="-":
            valid=True
        else:
            print("You can't Overwrite ")
    board[position]=player

    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    #set up global variable
    global winner
    #check rows
    row_winner=check_rows()
    #check columns
    column_winner=check_columns()
    #check diagnals
    diagonal_winner=check_diagonals()
    if row_winner:
        #there was win
        winner=row_winner
    elif column_winner:
        #there was win
        winner=column_winner
    elif diagonal_winner:
        #there wa win
        winner=diagonal_winner
    else:
        winner=None
        
    return
def check_rows():
    global game_still_going
    
    row_1=board[0]==board[1]== board[2] !="-"
    row_2=board[3]==board[4]== board[5] !="-"
    row_3=board[6]==board[7]== board[8] !="-"
    
    if row_1 or row_2 or row_3:
        game_still_going=False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns() :
    global game_still_going
    
    column_1=board[0]==board[3]== board[6] !="-"
    column_2=board[1]==board[4]== board[7] !="-"
    column_3=board[2]==board[5]== board[8] !="-"
    
    if column_1 or column_2 or column_3:
        game_still_going=False

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

    return


def check_diagonals():
    global game_still_going
    
    diagonal_1=board[0]==board[4]== board[8] !="-"
    diagonal_2=board[6]==board[4]== board[2] !="-"
    
    if diagonal_1 or diagonal_2:
        game_still_going=False

    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return




def check_if_tie() :
    global game_still_going
    if "-" not in board:
        game_still_going=False
    return

def flip_player():
    global current_player
    if current_player=="X":
        current_player="O"
    elif current_player=="O":
        current_player="X"

    return

play_game()

