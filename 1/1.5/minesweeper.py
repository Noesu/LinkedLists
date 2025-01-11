from random import sample

class Cell:
    def __init__(self, mine: bool, around_mines: int = None, fl_open: bool = False):
        self.mine = mine
        self.around_mines = around_mines
        self.fl_open = fl_open

    def __str__(self):
        if not self.fl_open:
            status = '#'
        else:
            if self.mine:
                status = '*'
            else:
                status = None
        return status


class GamePole:
    def init(self, m: int, n: int):
        self.size = m
        total_cells_count = pow(self.size, 2)
        mined_cells = sample(range(total_cells_count), n)
        cells_sequence = iter([True if cell in mined_cells else False for cell in range(total_cells_count)])
        self.pole = [[Cell(next(cells_sequence)) for cell in range(self.size)] for line in range(self.size)]
        self.calculate_around_mines()

    def show(self):
        for line in self.pole:
            print(' '.join(str(cell) for cell in line))

    def calculate_around_mines(self):
        for x, line in enumerate(self.pole):
            for y, cell in enumerate(line):
                if not cell.mine:
                    nearest_cells = self.collect_nearest_cells(x, y)
                    threat = 0
                    for x_pos, y_pos in nearest_cells:
                        if self.pole[x_pos][y_pos].mine:
                            threat += 1
                    self.pole[x][y].around_mines = threat
                else:
                    self.pole[x][y].around_mines = 0

    def collect_nearest_cells(self, x_pos: int, y_pos: int) -> list:
        nearest_cells = [(x, y)
                         for x in range(x_pos - 1, x_pos + 2)
                         for y in range(y_pos - 1, y_pos + 2)
                         if 0 <= x < self.size and 0 <= y < self.size and (x, y) != (x_pos, y_pos)
                         ]
        return nearest_cells


pole_game = GamePole()
pole_game.init(10, 12)
pole_game.show()
