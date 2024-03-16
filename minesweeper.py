import random


class Cell:
    """
    Класс для представления клетки игрового поля.

    :param around_mines: Количество мин вокруг клетки.
    :type around_mines: int
    :param mine: Флаг, указывающий наличие мины в клетке.
    :type mine: bool
    """

    def __init__(self, around_mines: int = 0, mine: bool = False) -> None:
        """
        Инициализация объекта клетки.

        :param around_mines: Количество мин вокруг клетки (по умолчанию 0).
        :type around_mines: int
        :param mine: Флаг, указывающий наличие мины в клетке (по умолчанию False).
        :type mine: bool
        """
        self.around_mines: int = around_mines
        self.mine: bool = mine
        self.fl_open: bool = False

    def __str__(self) -> str:
        """
        Возвращает строковое представление клетки.

        Если клетка не открыта, возвращается символ '#'.
        Если клетка содержит мину, возвращается символ '*'.
        Если клетка открыта и рядом есть мины, возвращается количество мин вокруг клетки в виде строки.

        :return: Строковое представление клетки.
        :rtype: str
        """
        if not self.fl_open:
            return "#"
        elif self.mine:
            return "*"
        else:
            return str(self.around_mines)


class GamePole:
    """
    Класс для представления игрового поля.
    """
    def __init__(self, size: int, mines: int) -> None:
        """
        Инициализирует игровое поле.

        :param size: Размер стороны игрового поля.
        :type size: int
        :param mines: Количество мин на поле.
        :type mines: int
        :raises ValueError: Количество мин превышает количество клеток на поле.
        """
        self.__size: int = size
        self.__mines: int = mines
        self.__create_pole(size)

    def __create_pole(self, size: int) -> None:
        """
        Создает игровое поле и заполняет его пустыми ячейками.

        :param size: Размер стороны игрового поля.
        :type size: int
        """
        self.__pole: list[list[Cell]] = [[Cell() for _ in range(size)] for _ in range(size)]
        self.__mine_planting()
        self.__count_mine_in_cell()

    def __mine_planting(self) -> None:
        """
        Размещает мины на игровом поле.
        :raises ValueError: Количество мин превышает количество клеток на поле.
        """

        if self.__mines > self.__size ** 2:
            raise ValueError("Количество мин превышает количество клеток на поле")

        mine_positions: list[int] = random.sample(range(self.__size ** 2), self.__mines)
        for position in mine_positions:
            row: int = position // self.__size
            col: int = position % self.__size
            self.__pole[row][col].mine = True

    def __count_mine_in_cell(self) -> None:
        """
        Считает количество мин в соседних ячейках для каждой клетки игрового поля.
        """
        for row in range(self.__size):
            for col in range(self.__size):
                self.__pole[row][col].around_mines = self.__count_mines(row, col)

    def __count_mines(self, row, col) -> int:
        """
        Считает количество мин в соседних ячейках для указанной клетки.

        :param row: Номер строки клетки.
        :type row: int
        :param col: Номер столбца клетки.
        :type col: int
        :return: Количество мин в соседних клетках.
        :rtype: int
        """
        count: int = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= row + i < self.__size and 0 <= col + j < self.__size:
                    count += self.__pole[row + i][col + j].mine
        return count

    def show(self) -> None:
        """
        Выводит игровое поле на экран.
        """
        for row in self.__pole:
            print(*row)


p = GamePole(2, 6)
p.show()