class Solution:
    # backracking approach
    # TC : exhaustive
    # SC : O(n)-> n is length of word
    def backtrack(self,board,row,col,word,idx)->bool:
        # base
        if idx == len(word):
            return True
        if row < 0 or row == self.m or col < 0 or col == self.n or board[row][col] == "#":
            return False
        # logic
        if board[row][col] == word[idx]:
            
            # action
            temp = board[row][col]
            board[row][col] = '#'
            # recurse
            for x,y in self.directions:
                newrow,newcol = x+row,y+col
                if self.backtrack(board,newrow,newcol,word,idx+1):
                    return True
            # backtrack
            board[row][col] = temp
        return False


    def exist(self, board: List[List[str]], word: str) -> bool:
        if board is None or word is None:
            return False
        self.m,self.n = len(board),len(board[0])
        self.directions = [ (-1,0),(1,0),(0,-1),(0,1)]
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0]:
                    if self.backtrack(board,i,j,word,0):
                        return True
        return False