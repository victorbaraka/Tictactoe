""" 
TicTacToe -------------------------------------------------"""

import random

class TicTactoe:
    def __init__(self):
        self.board = []

#creating the board layout
    def create_board (self):
        for i in range (3):
            row = []
            for j in range (3):
                row.append("-")
                self.row.append(row)
    
    def get_random_player_first(self):
        return random.randint(0,1)
    

    def fix_spot(self,row,col,player):
        self.board [row][col] = player
        board_values =  set()

        #check rows
        for i in range(n):
            for j in range (n):
                board_values.add(self.board[i][j])
                if board_values == {player}:
                    return True
                else:
                    board_values.clear()

        #check cols
        for i in range (n):
            for j in range (n):
                board_values.add(self.board[j][i])
                if  board_values == {player}:
                    return True
                else :
                    board_values.clear()

        #check diagonals
        for i in range(n):
            board_values.add(self.board[0][2])
            board_values.add(self.board[1][1])
            board_values.add(self.board[2][0])
            if board_values == {player}:
                return True
            else:
                return False

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
                else:
                    return True
    
    def swap_player_turn

   