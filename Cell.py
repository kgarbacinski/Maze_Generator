class Cell:
    def __init__(self, x, y, col, row):
        self.x = x
        self.y = y
        self.row = row
        self.col = col
        self._visited = False

        self.solution_cell = None
    @property
    def visited(self):
        return self._visited

    @visited.setter
    def visited(self, state):
        self._visited = state

    def set_dir(self, dir):
        self.dir = dir
