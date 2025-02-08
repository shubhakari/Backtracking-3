class Solution:

    def captureBoard(self,board:List[List[str]],n:int) -> None:
        temparr = []
        for i in range(n):
            tempstr = ""
            for j in range(n):
                tempstr += board[i][j]
            temparr.append(tempstr)
        self.res.append(temparr)

    def checkBoard(self,board: List[List[str]],n:int,row:int,col:int) -> bool:
        # col - wise iteration
        for i in range(n):
            if board[i][col] == "Q":
                return False
        # left-diagnol check
        i,j = row,col
        while i >=0 and j >=0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1
        # right-diagnol check
        i,j = row,col
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1
        return True

    def backtrack(self,board: List[List[str]],n:int,row:int) -> None:
        if row == n:
            self.captureBoard(board,n)
            return
        for col in range(n):
            if self.checkBoard(board,n,row,col):
                # action
                board[row][col] = "Q"
                # recurse
                self.backtrack(board,n,row+1)
                # undo
                board[row][col] = "."

    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return []
        board = [["."] * n for _ in range(n)]
        self.res = []
        self.backtrack(board,n,0)
        return self.res
        