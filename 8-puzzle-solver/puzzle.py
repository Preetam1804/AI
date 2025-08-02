class Puzzle:
    def __init__(self, board, parent=None, action=None):
        self.board = board
        self.parent = parent
        self.action = action
        if parent:
            self.g = parent.g + 1
        else:
            self.g = 0

    def __repr__(self):
        state=""
        for r, row in enumerate(self.board):
            for c, value in enumerate(row):
                state += f"{value} "
            state += "\n"
        return state

    def find_blank(self):
        for r, row in enumerate(self.board):
            for c, value in enumerate(row):
                if value == 0:
                    return r, c
        return None
    def copy(self):
        copy=[]
        for i in self.board:
                copy.append(i.copy())
        return copy
    def get_neighbors(self):
        neighbors=[]
        moves = [(-1, 0, 'UP'), (1, 0, 'DOWN'), (0, -1, 'LEFT'), (0, 1, 'RIGHT')]
        r,c=self.find_blank()
        for i,j,k in moves:
            nr,nc=r+i,c+j
            if(nr>=0 and nr<3 and nc>=0 and nc<3):
                copied_board=self.copy()
                copied_board[r][c], copied_board[nr][nc] = copied_board[nr][nc], copied_board[r][c]
                neighbors.append(Puzzle(copied_board, parent=self, action=k))

        return neighbors