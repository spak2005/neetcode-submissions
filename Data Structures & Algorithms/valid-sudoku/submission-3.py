class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_checker = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row_checker:
                    return False
                else:
                    row_checker.add(board[i][j])
        
        for i in range(9):
            col_checker = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in col_checker:
                    return False
                else:
                    col_checker.add(board[j][i])
        
        store = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                key = (i//3, j//3)
                if key not in store:
                    store[key] = set() 
                
                if board[i][j] in store[key]:
                    return False
                else:
                        store[key].add(board[i][j])
        return True 




                

