class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = {}
        section_map = {}
        col_map = {}

        def get_section(row,col):
            if row < 3:
                return 1 if col <3 else 2 if col <6 else 3
            if row < 6:
                return 4 if col <3 else 5 if col <6 else 6
            if row < 9:
                return 7 if col <3 else 8 if col <6 else 9

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == '.':
                    continue
                section = get_section(row,col)
                if not section_map.get((section,board[row][col])):
                    section_map[(section,board[row][col])] = True
                else:
                    return False
                if not row_map.get((row,board[row][col])):
                    row_map[(row,board[row][col])] = True
                else:
                    return False
                if not col_map.get((col,board[row][col])):
                    col_map[(col,board[row][col])] = True
                else:
                    return False
        return True
        