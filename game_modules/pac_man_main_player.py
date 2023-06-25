# Создание главного героя игры PAC MAN

import pygame


# Работа с изображениями главного героя.
initial_position_x = 425
initial_position_y = 663

main_character = []

for i in range(1, 5):
    # изображение 1, 2, 3, 4
    # pygame.transform.scale - изменяет размер картинки (45, 45)
    # pygame.image.load - загружает картинку
    main_character.append(
        pygame.transform.scale(
            pygame.image.load(fr'game_modules/img_game/main_character_graphics/{i}.png'),
            (45, 45)))


def creating_a_protagonist(screen, direction, counter):
    """Рисование игрока, согласно его расположению в пространстве"""
    # отрисовывание главного игрока поверх основного (screen) поля игры
    if direction == 0:
        # Направление - вправо
        # 5 - отвечает за выбор картинки игрока.
        screen.blit(main_character[counter // 5],
                    (initial_position_x, initial_position_y))

    elif direction == 1:
        # Направление - влево
        # screen.blit(pygame.transform.flip(main_character[counter // 5], True, False), (initial_position_x, initial_position_y))
        screen.blit(pygame.transform.rotate(main_character[counter // 5], 180),
                    (initial_position_x, initial_position_y))

    elif direction == 2:
        # Направление - ввверх
        screen.blit(pygame.transform.rotate(main_character[counter // 5], 90),
                    (initial_position_x, initial_position_y))

    elif direction == 3:
        # Направление - вниз
        screen.blit(pygame.transform.rotate(main_character[counter // 5], 90),
                    (initial_position_x, initial_position_y))
