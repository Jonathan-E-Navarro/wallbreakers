from collections import defaultdict
class Solution:
    def __init__(self):
        self.box_index = None
        self.rows = None
        self.columns = None
        self.boxes = None 
        self.sudoku_solved = None
        self.n = None
        self.N = None
        
    def could_place(self,d, row, col):
            #Check if putting a number d in (row, col) is valid
            return not (d in self.rows[row] or d in self.columns[col] or \
                    d in self.boxes[self.box_index(row, col)])
        
    def place_number(self, d, row, col):
            #put number in (row, col) 
            self.rows[row][d] += 1
            self.columns[col][d] += 1
            self.boxes[self.box_index(row, col)][d] += 1
            self.board[row][col] = str(d)
    
    def remove_number(self, d, row, col):
            #Remove a number that didn't work out so we can backtrack
            del self.rows[row][d]
            del self.columns[col][d]
            del self.boxes[self.box_index(row, col)][d]
            self.board[row][col] = '.'    
            
    def place_next_numbers(self,row, col):
            #Call backtrack function in recursion to continue to place numbers
            #till the moment we have a solution
    
            # if we're in the last column and last row then we've gon through successfullly 
            if col == self.N - 1 and row == self.N - 1:
                self.sudoku_solved = True
                   
            else:
                # if we're in the end of the row
                # go to the next row
                if col == self.N - 1:
                    self.backtrack(row + 1, 0)
                # go to the next column
                else:
                    self.backtrack(row, col + 1)
    
    def backtrack(self, row = 0, col = 0):
            # if the cell is empty
            if self.board[row][col] == '.':
                # iterate over all numbers from 1 to 9
                for d in range(1, 10):
                    if self.could_place(d, row, col):
                        self.place_number(d, row, col)
                        self.place_next_numbers(row, col)
                        # if sudoku is solved, there is no need to backtrack
                        # since the single unique solution is promised
                        if not self.sudoku_solved:
                            self.remove_number(d, row, col)
            else:
                self.place_next_numbers(row, col)
                
                
    def solveSudoku(self, board: List[List[str]]) -> None:
        # box size
        self.n = 3
        # row size
        self.N = 3 * 3
        # lambda function to compute box index
        self.box_index = lambda row, col: (row // self.n ) * self.n + col // self.n
        # init rows, columns and boxes
        self.rows = [defaultdict(int) for i in range(self.N)]
        self.columns = [defaultdict(int) for i in range(self.N)]
        self.boxes = [defaultdict(int) for i in range(self.N)]
        self.board = board
        
        for i in range(self.N):
            for j in range(self.N):
                if self.board[i][j] != '.': 
                    d = int(self.board[i][j])
                    self.place_number(d, i, j)
        
        self.sudoku_solved = False
        self.backtrack()