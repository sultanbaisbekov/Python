import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Машинка на дороге")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Настройки машины
car_width = 60
car_height = 120
car_x = screen_width // 2 - car_width // 2
car_y = screen_height - car_height - 20
car_speed = 5

# Функция для рисования машины
def draw_car(x, y):
    pygame.draw.rect(screen, RED, (x, y, car_width, car_height))  # Машинка

# Главный игровой цикл
def game_loop():
    global car_x, car_y

    # Скорость перемещения машины
    move_x = 0
    move_y = 0

    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)  # Фон экрана

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Управление машиной
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            move_x = -car_speed
        elif keys[pygame.K_RIGHT]:
            move_x = car_speed
        else:
            move_x = 0

        if keys[pygame.K_UP]:
            move_y = -car_speed
        elif keys[pygame.K_DOWN]:
            move_y = car_speed
        else:
            move_y = 0

        # Обновляем позицию машины
        car_x += move_x
        car_y += move_y

        # Ограничение движения, чтобы машина не выходила за пределы экрана
        if car_x < 0:
            car_x = 0
        if car_x > screen_width - car_width:
            car_x = screen_width - car_width
        if car_y < 0:
            car_y = 0
        if car_y > screen_height - car_height:
            car_y = screen_height - car_height

        # Рисуем машину
        draw_car(car_x, car_y)

        # Обновляем экран
        pygame.display.update()

        # Частота кадров
        clock.tick(60)

# Запуск игры
game_loop()
