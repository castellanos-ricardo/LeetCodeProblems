from collections import defaultdict

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #create a dictionary for rows and cols
        rows =defaultdict(set) 
        cols = defaultdict(set) 
        
        #create a hash
        squares = defaultdict(set) 
        
        for r in range(9):
            for c in range(9):
                #check if element is empty
                if (board[r][c] == '.'):
                    continue
                if(board[r][c] in rows[r] or
                  board[r][c] in cols[c] or
                  board[r][c] in squares[(r//3, c//3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True
