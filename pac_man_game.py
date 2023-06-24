# PAC MAN GAME
# Python 3.10
import pygame

# импорт уровня доски Игры.
from game_modules.board_level import game_board_level
from game_modules.drawing_elements import drawing_element

# Инициализация PyGame
pygame.init()
pygame.font.init()

# Начальные данные.
# Константы размера поля.
HEIGHT_BOARD = 950
WIDTH_BOARD = 900

screen = pygame.display.set_mode([WIDTH_BOARD, HEIGHT_BOARD])
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('game_modules/FreeSans.ttf', 15)
level = game_board_level


def draw_board():
    """Заполнение элементами поля уровня"""
    cell_height = (HEIGHT_BOARD - 50) // 32
    cell_width = WIDTH_BOARD // 30

    row_count = len(level)
    """Количество строк в поле уровня"""

    for i in range(row_count):  # идём по строкам
        cell_counter_in_a_row = len(level[i])
        for j in range(cell_counter_in_a_row):  # идём по ячейкам
            drawing_element(i, j, screen, cell_height, cell_width)


# "Бесконечный" Цикл Игры.
game_cycle = True

while game_cycle:
    timer.tick(fps)
    screen.fill('black')

    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_cycle = False

    pygame.display.flip()

pygame.quit()
