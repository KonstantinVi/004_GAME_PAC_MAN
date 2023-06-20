# PAC MAN GAME
# Python 3.10
import pygame

# импорт доски Игры.
from board_level import game_board_level


# Инициализация PyGame
pygame.init()
pygame.font.init()


# Начальные данные.
# Константы размера поля.
WIDTH_BOARD = 900
HEIGHT_BOARD = 950


screen = pygame.display.set_mode([WIDTH_BOARD, HEIGHT_BOARD])
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesans.ttf', 15)

# Бесконечный Цикл Игры.
game_cycle = True

while game_cycle:
    timer.tick(fps)
    screen.fill('black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_cycle = False

    pygame.display.flip()

pygame.quit()