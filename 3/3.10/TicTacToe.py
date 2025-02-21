from typing import Any, Optional, Set, Tuple

class Cell:
    def __init__(self) -> None:
        self.reset()

    def __bool__(self) -> bool:
        """Признание объекта класса Cell правдивым, если он пустой"""
        return not self.value

    def __repr__(self) -> str:
        """Определение представления ячейки"""
        if self.value == 0:
            return '.'
        elif self.value == 1:
            return 'X'
        elif self.value == 2:
            return 'O'
        else:
            raise ValueError(f'Некорректное значение ячейки: {self.value}')

    def reset(self) -> None:
        """Обнуление параметров ячейки"""
        self.is_free = True
        self.value = 0


class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2
    COL_INDEX = {"A": 0, "А": 0, "B": 1, "В": 1, "C": 2, "С": 2}
    VICTORY_CONDITIONS = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]


    def __init__(self) -> None:
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))
        self.human_cells: Set[Tuple[int, int]] = set()
        self.computer_cells: Set[Tuple[int, int]] = set()
        self.is_human_win = False
        self.is_computer_win = False
        self.is_draw = False

    def __bool__(self) -> bool:
        """Признание партии игры правдивой если она не закончена """
        return not any([self.is_draw, self.is_human_win, self.is_computer_win])

    def __len__(self) -> int:
        """Определение длины партии как количества занятых на поле ячеек"""
        return len(self.computer_cells) + len(self.human_cells)

    @property
    def is_human_win(self) -> bool:
        return self.__is_human_win

    @is_human_win.setter
    def is_human_win(self, value: bool) -> None:
        self.__is_human_win = value

    @property
    def is_computer_win(self) -> bool:
        return self.__is_computer_win

    @is_computer_win.setter
    def is_computer_win(self, value: bool) -> None:
        self.__is_computer_win = value

    @property
    def is_draw(self) -> bool:
        return self.__is_draw

    @is_draw.setter
    def is_draw(self, value: bool) -> None:
        self.__is_draw = value

    def __getitem__(self, coords: Tuple[int, int]) -> int:
        r, c = coords
        self.__validate_cell_exists(r, c)
        return self.pole[r][c].value

    def __setitem__(self, coords: Tuple[int, int], value: int):
        r, c = coords
        self.__validate_cell_exists(r, c)
        self.__validate_cell_is_free(r, c)
        self.pole[r][c].value = value
        self.pole[r][c].is_free = False
        if value == TicTacToe.HUMAN_X:
            self.human_cells.add((r, c))
        elif value == TicTacToe.COMPUTER_O:
            self.computer_cells.add((r, c))
        self.__check_victory()

    @staticmethod
    def __clear_screen() -> None:
        print('\n' * 80)

    @staticmethod
    def __validate_cell_exists(r: int, c: int) -> None:
        if not (0 <= r < 3 and 0 <= c < 3):
            raise IndexError("неверный индекс клетки")

    def __validate_cell_is_free(self, r: int, c: int) -> None:
        if not self.pole[r][c].is_free:
            raise ValueError('клетка уже занята')

    def __validate_human_step(self, user_input: Any) -> Tuple[Optional[int], Optional[int], Optional[str]]:
        """Проверка корректности пользовательского ввода"""
        # Проверяем, что введено 2 символа
        if len(user_input) != 2:
            return None, None, f'Некорректный ввод: {user_input}'

        # Если первый символ - цифра, то она преобразуется в индекс, а второй индекс получаем из словаря
        if user_input[0].isdigit():
            r = int(user_input[0]) - 1
            c = TicTacToe.COL_INDEX.get(user_input[1].upper())
        # Если второй символ - цифра, то она преобразуется в индекс, а первый индекс получаем из словаря
        elif user_input[1].isdigit():
            c = TicTacToe.COL_INDEX.get(user_input[0].upper())
            r = int(user_input[1]) - 1
        # Если ни один символ не является цифрой, то возвращаем сообщение об ошибке
        else:
            return None, None, f'Некорректный ввод: {user_input}'

        # Если в словаре не найдено совпадений индекса для введенного символа, то возвращаем сообщение об ошибке
        if r is None or c is None:  # Проверяем, что индексы валидны
            return None, None, f'Некорректный ввод: {user_input}'

        # Проверяем находится ли клетка в диапазоне поля и свободна ли клетка
        try:
            self.__validate_cell_exists(r, c)
            self.__validate_cell_is_free(r, c)
        except (IndexError, ValueError) as e:
            return None, None, str(e)

        # Возвращаем корректный индекс
        return r, c, None

    def __check_victory(self) -> None:
        """Определение победителя при наличии линии, занятой крестиками или ноликами, либо определение ничьей"""
        for winning_line in TicTacToe.VICTORY_CONDITIONS:
            if set(winning_line).issubset(self.computer_cells):
                self.is_computer_win = True
                break
            elif set(winning_line).issubset(self.human_cells):
                self.is_human_win = True
                break
        else:
            if len(self) == 9:
                self.is_draw = True

    def init(self) -> None:
        """Инициализация игры"""
        self.__init__()

    def show(self, status_line: Optional[str]=None) -> None:
        """Отображение статусной строки и текущего состояния игрового поля"""
        self.__clear_screen()
        if status_line:
            print(status_line)
        displayed_row_number = 1
        print('  A B C')
        for line in self.pole:
            print(displayed_row_number, end=' ')
            for cell in line:
                print(cell, end=' ')
            displayed_row_number += 1
            print()

    def human_go(self) -> None:
        """Реализация хода игрока"""
        error_message = None
        while True:
            self.show(error_message)
            human_step = input('Введите координаты хода: ')
            r, c, error_message = self.__validate_human_step(human_step)
            if not error_message:
                self[r, c] = TicTacToe.HUMAN_X
                break

    def computer_go(self) -> None:
        """Реализация хода компьютера"""
        for r in range(3):
            for c in range(3):
                if self.pole[r][c].is_free:
                    self[r, c] = TicTacToe.COMPUTER_O
                    return


########################################################################################################################


cell = Cell()
assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
cell.value = 1
assert bool(cell) == False, "функция bool для объекта класса Cell вернула неверное значение"

assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(TicTacToe, 'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"

game = TicTacToe()
assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
assert game[0, 0] == 0 and game[2, 2] == 0, "неверные значения ячеек, взятые по индексам"
game[1, 1] = TicTacToe.HUMAN_X
assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game[0, 0] = TicTacToe.COMPUTER_O
assert game[0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game.init()
assert game[0, 0] == TicTacToe.FREE_CELL and game[1, 1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"

try:
    game[3, 0] = 4
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

game.init()
assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"

game[0, 0] = TicTacToe.HUMAN_X
game[1, 1] = TicTacToe.HUMAN_X
game[2, 2] = TicTacToe.HUMAN_X
assert game.is_human_win and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

game.init()
game[0, 0] = TicTacToe.COMPUTER_O
game[1, 0] = TicTacToe.COMPUTER_O
game[2, 0] = TicTacToe.COMPUTER_O
assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

########################################################################################################################

# game = TicTacToe()
# game.init()
# step_game = 0
# while game:
#     game.show()
#     if step_game % 2 == 0:
#         game.human_go()
#     else:
#         game.computer_go()
#     step_game += 1
#
# game.show()
#
# if game.is_human_win:
#     print("Поздравляем! Вы победили!")
# elif game.is_computer_win:
#     print("Все получится, со временем")
# else:
#     print("Ничья.")
