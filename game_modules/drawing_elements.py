# РИСУЕМ ЭЛЕМЕНТЫ КАРТЫ

import pygame
import math
# Импорт уровня доски Игры.
from game_modules import board_level


def draw_board(HEIGHT_BOARD, WIDTH_BOARD, screen, level):
    """Заполнение элементами поля уровня"""

    cell_height = (HEIGHT_BOARD - 50) // 32
    cell_width = WIDTH_BOARD // 30

    row_count = len(level)
    """Количество строк в поле уровня"""

    # Рисуем карту уровня игры по клеточкам.
    for i in range(row_count):  # идём по строкам
        cell_counter_in_a_row = len(level[i])
        for j in range(cell_counter_in_a_row):  # идём по ячейкам

            if level[i][j] == 1:
                # Рисуем точку.
                pygame.draw.circle(screen,
                                   'white',
                                   (j * cell_width + (cell_width * 0.5),
                                   i * cell_height + (cell_height * 0.5)),
                                   4,
                                   )

            elif level[i][j] == 2:
                # Рисуем жирную точку.
                pygame.draw.circle(screen,
                                   'white',
                                   (j * cell_width + (cell_width * 0.5),
                                    i * cell_height + (cell_height * 0.5)),
                                   10,
                                   )

            elif level[i][j] == 3:
                # Рисуем вертикальную линию.
                pygame.draw.line(screen,
                                 'blue',
                                 (j * cell_width + (cell_width * 0.5), i * cell_height),
                                 (j * cell_width + (cell_width * 0.5), i * cell_height + cell_height),
                                 2,
                                 )

            elif level[i][j] == 4:
                # Рисуем горизонтальную линию.
                pygame.draw.line(screen,
                                 'blue',
                                 (j * cell_width , i * cell_height + (cell_height * 0.5)),
                                 (j * cell_width + cell_width, i * cell_height + (cell_height * 0.5)),
                                 2,
                                 )

            elif level[i][j] == 5:
                # Рисуем четверть круга (по часам: с 12 до 3).
                pygame.draw.arc(screen,
                                'blue',
                                [(j * cell_width - (cell_width * 0.4)) - 2,
                                 (i * cell_height + cell_height * 0.5),
                                 cell_width,
                                 cell_height],
                                0,
                                math.pi / 2,
                                2,
                                )

            elif level[i][j] == 6:
                # Рисуем четверть круга (по часам: с 9 до 12).
                pygame.draw.arc(screen,
                                'blue',
                                [(j * cell_width + (cell_width * 0.5)),
                                 (i * cell_height + cell_height * 0.5),
                                 cell_width,
                                 cell_height],
                                math.pi / 2,
                                math.pi,
                                2,
                                )

            elif level[i][j] == 7:
                # Рисуем четверть круга (по часам: с 6 до 9).
                pygame.draw.arc(screen,
                                'blue',
                                [(j * cell_width + cell_width * 0.5),
                                 (i * cell_height - cell_height * 0.4 - 1),
                                 cell_width,
                                 cell_height],
                                math.pi,
                                3 * math.pi / 2,
                                2,
                                )

            elif level[i][j] == 8:
                # Рисуем четверть круга (по часам: с 3 до 6).
                pygame.draw.arc(screen,
                                'blue',
                                [(j * cell_width - cell_width * 0.4 - 2),
                                 (i * cell_height - cell_height * 0.4 - 1),
                                 cell_width,
                                 cell_height],
                                3 * math.pi / 2,
                                2 * math.pi,
                                2,
                                )

            elif level[i][j] == 9:
                # Рисуем горизонтальную линию.
                pygame.draw.line(screen,
                                 'white',
                                 (j * cell_width, i * cell_height + (cell_height * 0.5)),
                                 (j * cell_width + cell_width, i * cell_height + (cell_height * 0.5)),
                                 2,
                                 )


if __name__ == '__main__':
    level = board_level.game_board_level
