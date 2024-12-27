from constants import *
import pygame

class Board:
    def __init__(self):
        # initialize the board
        self.board = []
        self.initialize_board()
        
    def initialize_board(self):
        """
        iterate over a list and create a 2D list that represents the 
        tictactoe board.
        """
        # 1st approach
        self.board = [["-" for i in range(3)] for j in range(3)]
    
    def print_board(self):
        """
        display the board by iterating over it's elements and printing them
        """
        for row in self.board: # row: ["-", "-", "-"]
            for col in row:
                print(col, end=" ")
                print()
                
    def available_square(self, row, col):
        """
        checks if the value of the given position on the sudoku board is '-'
        """
        return self.board[row][col] == '-'
    
    def mark_square(self, row, col, chip_type):
        """
        mark the given cell in the board with the given chip
        """
        self.board[row][col] = chip_type
        
    def board_is_full(self):
        """
        check if the board is full
        """
        for row in self.board:
            for chip in row:
                if chip == "-":
                    return False
        return True
            
    def check_if_winner(self, chip_type):
        """
        check for the winner of the board
        """
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] == chip_type:
                return True
            
        # check all columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == chip_type:
                return True
            if self.board[0][0] == self.board[1][1] == self.board[2][2] == chip_type:
                return True
            if self.board[0][2] == self.board[1][1] == self.board[2][0] == chip_type:
                return True
            return False
        
    # row: row index, col: col index
    def is_valid(self, row, col):
        """
        check if the current assignment is valid.
        for the assignment to be valid:
            1) cell must lie in the given box
            2) the value of the cell must be '-'
        """
        if 0 <= row <= 2 and 0 <= col <= 2 and self.available_square(row,col):
            return True
        return False
    
    def turn(self):
        """
            return the player whose turn it is to play.
        """
        count_x = sum([row.count(CHIP_X) for row in self.board])
        count_o = sum([row.count(CHIP_O) for row in self.board])
        
        return count_x <= count_o