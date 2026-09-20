class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # tracking if each box, row, col contains num
        box = [[False] * 10 for _ in range(10)]
        cols = [[False] * 10 for _ in range(10)]
        rows = [[False] * 10 for _ in range(10)]

        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value == ".":
                    continue
                value = int(value)
                box_index = ((col // 3) * 3) + (row // 3)
                print(f"row : {row}, col: {col}, box_index: {box_index}")
                if box[box_index][value] or rows[row][value] or cols[col][value]:
                    return False
                else:
                    box[box_index][value]= True
                    rows[row][value] = True
                    cols[col][value] = True
        
        return True

        