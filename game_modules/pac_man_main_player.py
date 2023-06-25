# Создание главного героя игры PAC MAN

import pygame


main_character = []

# Формируем список из изображений для динамичной картинки игрока.
for i in range(1, 5):
    # изображение 1, 2, 3, 4
    # pygame.transform.scale - изменяет размер картинки (45, 45)
    # pygame.image.load - загружает картинку
    main_character.append(
        pygame.transform.scale(
            pygame.image.load(fr'game_modules/img_game/main_character_graphics/{i}.png'),
            (45, 45)))


def creating_a_protagonist(screen,
                           direction,
                           counter,
                           initial_position_x,
                           initial_position_y):
    """Рисование игрока, согласно его расположению в пространстве"""
    # Рисование главного игрока поверх основного (screen) поля игры
    if direction == 0:
        # Направление - вправо
        # 5 - отвечает за выбор картинки игрока.
        screen.blit(main_character[counter // 5],
                    (initial_position_x, initial_position_y))

    elif direction == 1:
        # Направление - влево
        screen.blit(pygame.transform.rotate(main_character[counter // 5], 180),
                    (initial_position_x, initial_position_y))

    elif direction == 2:
        # Направление - вверх
        screen.blit(pygame.transform.rotate(main_character[counter // 5], 90),
                    (initial_position_x, initial_position_y))

    elif direction == 3:
        # Направление - вниз
        screen.blit(pygame.transform.rotate(main_character[counter // 5], -90),
                    (initial_position_x, initial_position_y))


def check_position(level,
                   HEIGHT_BOARD,
                   WIDTH_BOARD,
                   direction,
                   initial_position_x,
                   initial_position_y):
    """Определяет степень свободы передвижения игрока"""
    # Центр координат игрока.
    center_pl_pos_x = initial_position_x + 24
    """Центр игрока по X"""
    center_pl_pos_y = initial_position_y + 23
    """Центр игрока по Y"""

    # Визуализация центра координат игрока.
    # pygame.draw.circle(screen, 'black', (center_pl_pos_x, center_pl_pos_y), 1)

    # Пути свободы: [вправо, влево, вверх, вниз].
    free_paths = [False, False, False, False]
    tmp_1 = (HEIGHT_BOARD - 50) // 32
    """Количество X-овых клеток"""
    tmp_2 = WIDTH_BOARD // 30
    """Количество Y-овых клеток"""
    tmp_3 = 15
    """Допуск для 'наезда' на соседнюю клетку"""

    if center_pl_pos_x // 30 < 29:
        # Игрок смотрит вправо.
        if direction == 0:
            if level[center_pl_pos_y // tmp_1][(center_pl_pos_x - tmp_3) // tmp_2] < 3:
                free_paths[1] = True

        # Игрок смотрит влево.
        if direction == 1:
            if level[center_pl_pos_y // tmp_1][(center_pl_pos_x + tmp_3) // tmp_2] < 3:
                free_paths[0] = True

        # Игрок смотрит вверх.
        if direction == 2:
            if level[(center_pl_pos_y + tmp_3) // tmp_1][center_pl_pos_x // tmp_2] < 3:
                free_paths[3] = True

        # Игрок смотрит вниз.
        if direction == 3:
            if level[(center_pl_pos_y - tmp_3) // tmp_1][center_pl_pos_x // tmp_2] < 3:
                free_paths[2] = True

        if direction in (2, 3):
            # Определение 'окна' шага игрока по X.
            if 12 <= (center_pl_pos_x % tmp_2) <= 18:
                if level[(center_pl_pos_y + tmp_3) // tmp_1][center_pl_pos_x // tmp_2] < 3:
                    free_paths[3] = True
                if level[(center_pl_pos_y - tmp_3) // tmp_1][center_pl_pos_x // tmp_2] < 3:
                    free_paths[2] = True

            # Определение 'окна' шага игрока по Y.
            if 12 <= (center_pl_pos_y % tmp_1) <= 18:
                if level[center_pl_pos_y // tmp_1][(center_pl_pos_x - tmp_2) // tmp_2] < 3:
                    free_paths[1] = True
                if level[center_pl_pos_y // tmp_1][(center_pl_pos_x + tmp_2) // tmp_2] < 3:
                    free_paths[0] = True


        if direction in (0, 1):
            # Определение 'окна' шага игрока по X.
            if 12 <= (center_pl_pos_x % tmp_2) <= 18:
                if level[(center_pl_pos_y + tmp_1) // tmp_1][center_pl_pos_x // tmp_2] < 3:
                    free_paths[3] = True
                if level[(center_pl_pos_y - tmp_1) // tmp_1][center_pl_pos_x // tmp_2] < 3:
                    free_paths[2] = True

            # Определение 'окна' шага игрока по Y.
            if 12 <= (center_pl_pos_y % tmp_1) <= 18:
                if level[center_pl_pos_y // tmp_1][(center_pl_pos_x - tmp_3) // tmp_2] < 3:
                    free_paths[1] = True
                if level[center_pl_pos_y // tmp_1][(center_pl_pos_x + tmp_3) // tmp_2] < 3:
                    free_paths[0] = True
    else:
        free_paths[0] = True
        free_paths[1] = True

    return free_paths


def player_movement(point_x, point_y, speed_player, direction, check_freedom):
    """Движение игрока"""
    if direction == 0 and check_freedom[0]:
        point_x += speed_player
    elif direction == 1 and check_freedom[1]:
        point_x -= speed_player
    if direction == 2 and check_freedom[2]:
        point_y -= speed_player
    elif direction == 3 and check_freedom[3]:
        point_y += speed_player
    return point_x, point_y


if __name__ == '__main__':
    pass
