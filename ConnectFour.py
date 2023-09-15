import numpy as np

class InputException(Exception): pass
class ColException(Exception): pass

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def get_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board,0))

def scan_for_win(board, piece):
    #check for a win
    #Vertical win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True
    
    #Horizontal win
    for i in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][i] == piece and board[r][i + 1] == piece and board[r][i + 2] == piece and board[r][i + 3] == piece:
                return True
    
    #Diagonal win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True
    
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True

board = create_board()
game_over = False
turn = 0

print_board(board)

while not game_over:
    col = None

    if turn == 0:
        #Player 1 turn
        while col == None:
            try:
                col = int(input("Player 1, Choose a column from 0 to 6: "))
                if not (col > -1 and col < 7):
                    raise InputException
                elif not board[5][col] == 0:
                    raise ColException
            except InputException:
                print("Please enter a valid input.")
                col = None
            except ColException:
                print("That column is full.")
                col = None
        #drop piece
        drop_piece(board, get_open_row(board, col), col, 1)

        if scan_for_win(board, 1):
            print("PLAYER 1 WINS!")
            game_over = True

        turn += 1
    else:
        #Player 2 turn
        while col == None:
            try:
                col = int(input("Player 2, Choose a column from 0 to 6: "))
                if not (col > -1 and col < 7):
                    raise InputException
                elif not board[5][col] == 0:
                    raise ColException
            except InputException:
                print("Please enter a valid input.")
                col = None
            except ColException:
                print("That column is full.")
                col = None
        
        #drop piece
        drop_piece(board, get_open_row(board, col), col, 2)

        if scan_for_win(board, 2):
            print("PLAYER 2 WINS!")
            game_over = True
    
        turn -= 1
    
    print_board(board)