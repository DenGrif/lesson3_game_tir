import pygame
import random

pygame.init()

SCREEN_WIDTH = 800import pygame
import random

pygame.init()

# Параметры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")

# Иконка игры
icon = pygame.image.load("img/Target.png")
pygame.display.set_icon(icon)

# Изображение цели
target_img = pygame.image.load("img/apple.png")
target_width = 50
target_height = 108

# Позиция цели
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Начальная скорость цели
target_speed_x = random.choice([0.1, 0.2])
target_speed_y = random.choice([0.1, 0.2])

# Случайный цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Счетчик очков
score = 0
font = pygame.font.Font(None, 36)

# Функция для отображения текста
def show_score():
    score_text = font.render(f"Очки: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

# Основной цикл игры
running = True
while running:
    screen.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Проверяем, попал ли игрок в цель
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1
                # Смена позиции цели
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                # Увеличение скорости при каждом попадании
                if target_speed_x > 0:
                    target_speed_x += 0.05  # Увеличиваем скорость вправо
                else:
                    target_speed_x -= 0.05  # Увеличиваем скорость влево
                if target_speed_y > 0:
                    target_speed_y += 0.05  # Увеличиваем скорость вниз
                else:
                    target_speed_y -= 0.05  # Увеличиваем скорость вверх

    # Движение цели
    target_x += target_speed_x
    target_y += target_speed_y

    # Отскок цели от границ экрана
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x = -target_speed_x
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y = -target_speed_y

    # Отображение цели и очков
    screen.blit(target_img, (target_x, target_y))
    show_score()

    pygame.display.update()

pygame.quit()

SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")

icon = pygame.image.load("img/Target.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/apple.png")
target_width = 50
target_height = 108

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

pygame.quit()
