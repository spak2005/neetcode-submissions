class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        store = {}
        for i in range(9):
            row_checker = set()
            col_checker = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row_checker:
                        return False
                    else:
                        row_checker.add(board[i][j])
            
                    key = (i//3, j//3)
                    if key not in store:
                        store[key] = set() 
                    if board[i][j] in store[key]:
                        return False
                    else:
                        store[key].add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in col_checker:
                            return False
                    else:
                        col_checker.add(board[j][i])
        return True 




                

