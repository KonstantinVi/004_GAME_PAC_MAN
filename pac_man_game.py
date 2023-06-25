# PAC MAN GAME
# Python 3.10
import pygame

# Импорт уровня доски игры.
from game_modules import board_level, drawing_elements
# Импорт главного героя.
from game_modules import pac_man_main_player


# Инициализация PyGame.
pygame.init()
pygame.font.init()

# Начальные данные.
# Константы размера поля.
HEIGHT_BOARD = 950
"""Высота игрового поля"""
WIDTH_BOARD = 900
"""Ширина игрового поля"""

screen = pygame.display.set_mode([WIDTH_BOARD, HEIGHT_BOARD])
"""Поле игры"""
# Установка title окна игры.
pygame.display.set_caption('PAC MAN Game')
timer = pygame.time.Clock()
"""Создание объекта 'Таймер обновления'"""
fps = 60
"""Частота кадров в секунду"""
direction = 0
counter = 0
flicker = True
font = pygame.font.Font('game_modules/FreeSans.ttf', 15)
level = board_level.game_board_level
"""Разметка уровня игры"""


# Основной цикл игры.
game_cycle = True

while game_cycle:
    # Таймер обновления экрана.
    timer.tick(fps)
    screen.fill('black')

    # Счётчик итераций.
    # Счётчик отвечает за частоту обновления кадра картинки игрока.
    if counter < 19:
        counter += 1
        if (counter > 10) and (counter < 15):
            flicker = True
    else:
        counter = 0
        flicker = False

    # Рисование поля игры.
    drawing_elements.draw_board(HEIGHT_BOARD,
                                WIDTH_BOARD,
                                screen,
                                level,
                                flicker)

    # Загрузка главного героя игры.
    pac_man_main_player.creating_a_protagonist(screen,
                                               direction,
                                               counter)

    # Определяет степень свободы движения игрока.
    pac_man_main_player.check_position(level,
                                       HEIGHT_BOARD,
                                       WIDTH_BOARD,
                                       direction)

    for event in pygame.event.get():

        # Выход из цикла через кнопку закрыть окно.
        if event.type == pygame.QUIT:
            game_cycle = False

        # Определение направления игрока, с помощью клавиатуры.
        if event.type == pygame.KEYDOWN:
            # Игрок смотрит вправо.
            if event.key == pygame.K_RIGHT:
                direction = 0
            # Игрок смотрит влево.
            if event.key == pygame.K_LEFT:
                direction = 1
            # Игрок смотрит вверх.
            if event.key == pygame.K_UP:
                direction = 2
            # Игрок смотрит вниз.
            if event.key == pygame.K_DOWN:
                direction = 3

    pygame.display.flip()

# ДеИнициализация PyGame.
pygame.quit()
