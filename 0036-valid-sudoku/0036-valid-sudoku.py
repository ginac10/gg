class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        temp = set()
        #check rows
        for row in board:#e.g. ["5","3",".",".","7",".",".",".","."]
            for num in row:
                if num != ".":
                    if num in temp:
                        return False
                    temp.add(num)
            temp = set()
        
        temp = set()
        #check cols
        for i in range(9):
            for j in range(9):
                num = board[j][i] #accidently did [i][j]
                if num != ".":
                    if num in temp:
                        return False
                    temp.add(num)  
            temp = set()
        
        temp = set()
        #check boxes
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                for i in range(3):
                    for j in range(3):
                        num = board[r+i][c+j]
                        if num != ".":
                            if num in temp:
                                return False
                            temp.add(num)
                temp = set()
                 
        return True