class Solution:
    
    ROWLEN = 0
    COLLEN = 0
    WORD = ''
    AVAILABLE_MOVES = [(1,0),(-1,0),(0,1),(0,-1)]
    
    def backtrack(self, board, row, col, curPos, visitedGrids):
        
        if row == self.ROWLEN or row < 0 or col == self.COLLEN or col < 0:
            return False
        
        if visitedGrids[row][col]:
            return False
        
        if board[row][col] != self.WORD[curPos]:
            return False
        
        if curPos == len(self.WORD) - 1:
            return True
        
        for move in self.AVAILABLE_MOVES:
            visitedGrids[row][col] = True
            
            if(self.backtrack(board, row + move[0], col + move[1], curPos + 1, visitedGrids)):
                return True
            
            visitedGrids[row][col] = False
            
        return False
        
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        self.ROWLEN = len(board)
        self.COLLEN = len(board[0])
        self.WORD = word
        
        visitedGrids = [[False for col in range(self.COLLEN)] for row in range(self.ROWLEN)]
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.backtrack(board, row, col, 0, visitedGrids):
                    return True
                
        return False
        
