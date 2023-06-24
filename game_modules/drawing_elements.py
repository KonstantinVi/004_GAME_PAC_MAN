# РИСУЕМ ЭЛЕМЕНТЫ КАРТЫ

import pygame
# импорт уровня доски Игры.
from game_modules.board_level import game_board_level

level = game_board_level


def drawing_element(i, j, screen, cell_height, cell_width):
    if level[i][j] == 1:
        # рисование точки
        pygame.draw.circle(screen,
                           'white',
                           (j * cell_width + (cell_width * 0.5),
                           i * cell_height + (cell_height * 0.5)),
                           4,
                           )

    elif level[i][j] == 2:
        # рисование жирной точки
        pygame.draw.circle(screen,
                           'white',
                           (j * cell_width + (cell_width * 0.5),
                            i * cell_height + (cell_height * 0.5)),
                           10,
                           )

    elif level[i][j] == 3:
        # рисование вертикальной линии
        pygame.draw.line(screen,
                         'blue',
                         (j * cell_width + (cell_width * 0.5), i * cell_height),
                         (j * cell_width + (cell_width * 0.5), i * cell_height + cell_height),
                         2,
                         )

    elif level[i][j] == 4:
        # рисование горизонтальной линии
        pygame.draw.line(screen,
                         'blue',
                         (j * cell_width , i * cell_height + (cell_height * 0.5)),
                         (j * cell_width + cell_width, i * cell_height + (cell_height * 0.5)),
                         2,
                         )


if __name__ == '__main__':
    pass
