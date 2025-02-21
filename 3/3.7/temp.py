import random

def isolated(ships: list) -> bool:
    """Формирование списка смежных точек для каждой точки из списка координат и проверка их совпадений"""
    for x_pos, y_pos in ships:
        surrounding_spaces = [(x, y)
                              for x in range(x_pos - 1, x_pos + 2)
                              for y in range(y_pos - 1, y_pos + 2)
                              if 0 <= x < N and 0 <= y < N and (x, y) != (x_pos, y_pos)
                             ]
        if any(space in ships for space in surrounding_spaces):
            return False
    return True


def get_ship_coordinates() -> list:
    """Формировние списка координат"""
    field_coordinates = [(x, y) for x in range(N) for y in range(N)]
    return random.sample(field_coordinates, 10)


random.seed(1)
N = int(input())
while True:                              # Начало бесконечного цикла
    ships = get_ship_coordinates()       # Получение списка координат
    if isolated(ships):                  # Проверка изолированности точке в списке координат
        P = [[0] * N for _ in range(N)]  # Формирование пустого поля
        for x, y in ships:               # Итерация по точкам в списке координат
            P[x][y] = 1                  # Размещение точки на поле
        break                            # Остановка бесконечного цикла