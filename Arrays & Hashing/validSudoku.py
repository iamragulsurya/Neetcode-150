class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = [0] * 10
            col = [0] * 10
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    row[num] += 1
                    if row[num] > 1: return False
            for j in range(9):
                if board[j][i] != '.':
                    num = int(board[j][i])      
                    col[num] += 1
                    if col[num] > 1: return False
    
        for i in range(9):
            row = (i//3) * 3
            col = (i%3) * 3
            nums = [0] * 10
            for j in range(row, row+3):
                for k in range(col, col+3):
                    if board[j][k] != '.':
                        num = int(board[j][k])
                        nums[num] += 1
                        if nums[num] > 1: return False
        return True