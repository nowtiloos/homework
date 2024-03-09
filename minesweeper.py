import random


class Cell:
    def __init__(self, around_mines=0, mine=False) -> None:
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False

    def __str__(self) -> str:
        if not self.fl_open:
            return "#"
        elif self.mine:
            return "*"
        else:
            return str(self.around_mines)


class GamePole:
    def __init__(self, size, mines) -> None:
        self.size = size
        self.mines = mines
        self.pole = self.create_pole(size, mines)

    def create_pole(self, size, mines) -> list[list[Cell]]:
        # создаю поле с пустыми ячейками
        pole = [[Cell() for _ in range(size)] for _ in range(size)]

        # рандомно заполняю минами
        mine_positions = random.sample(range(size ** 2), mines)
        for position in mine_positions:
            row = position // size
            col = position % size
            pole[row][col].mine = True

        # считаю количество мин в соседних ячейках
        for row in range(size):
            for col in range(size):
                pole[row][col].around_mines = self.count_mines(pole, row, col)

        return pole

    def count_mines(self, pole, row, col) -> int:
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= row + i < self.size and 0 <= col + j < self.size:
                    count += pole[row + i][col + j].mine
        return count

    def show(self) -> None:
        for row in self.pole:
            print(*row)
