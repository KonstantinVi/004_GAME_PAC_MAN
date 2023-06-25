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
direction_command = 0
speed_player = 2
"""Скорость движения игрока"""
font = pygame.font.Font('game_modules/FreeSans.ttf', 15)
level = board_level.game_board_level
"""Разметка уровня игры"""

# Работа с изображениями главного героя.
initial_position_x = 425
"""Начальная позиция игрока по Y"""
initial_position_y = 663
"""Начальная позиция игрока по X"""


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
                                               counter,
                                               initial_position_x,
                                               initial_position_y)

    # Определяет степень свободы движения игрока.
    check_freedom = pac_man_main_player.check_position(level,
                                                       HEIGHT_BOARD,
                                                       WIDTH_BOARD,
                                                       direction,
                                                       initial_position_x,
                                                       initial_position_y)

    # координаты движения игрока
    initial_position_x, \
        initial_position_y = pac_man_main_player.player_movement(initial_position_x,
                                                                 initial_position_y,
                                                                 speed_player,
                                                                 direction,
                                                                 check_freedom)

    for event in pygame.event.get():

        # Выход из цикла через кнопку закрыть окно.
        if event.type == pygame.QUIT:
            game_cycle = False

        # Определение направления игрока, с помощью клавиатуры.
        # Нажатие клавиши.
        if event.type == pygame.KEYDOWN:
            # Игрок смотрит вправо.
            if event.key == pygame.K_RIGHT:
                direction_command = 0
            # Игрок смотрит влево.
            if event.key == pygame.K_LEFT:
                direction_command = 1
            # Игрок смотрит вверх.
            if event.key == pygame.K_UP:
                direction_command = 2
            # Игрок смотрит вниз.
            if event.key == pygame.K_DOWN:
                direction_command = 3

        # Отпуск клавиши.
        if event.type == pygame.KEYUP:
            # Игрок смотрит вправо.
            if event.key == pygame.K_RIGHT and direction_command == 0:
                direction_command = direction
            # Игрок смотрит влево.
            if event.key == pygame.K_LEFT and direction_command == 1:
                direction_command = direction
            # Игрок смотрит вверх.
            if event.key == pygame.K_UP and direction_command == 2:
                direction_command = direction
            # Игрок смотрит вниз.
            if event.key == pygame.K_DOWN and direction_command == 3:
                direction_command = direction

    # Куда игрок может идти.
    for i in range(4):
        if direction_command == i and check_freedom[i]:
            direction = i

    if initial_position_x > 900:
        initial_position_x = -47
    elif initial_position_x < -50:
        initial_position_x = 897

    pygame.display.flip()

# ДеИнициализация PyGame.
pygame.quit()
