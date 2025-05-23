import pygame
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")
pygame.display.set_icon(pygame.image.load("img/img.png"))

# Загрузка цели
raw_target = pygame.image.load("img/09_49_34.png")

# Задаём нужный размер
target_width, target_height = 200, 200
# Масштабируем изображение до 40×40
target_img = pygame.transform.scale(raw_target, (target_width, target_height))

# Теперь можно безопасно брать диапазон:
target_x = random.randint(0, SCREEN_WIDTH  - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Случайный фон
color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
             mouse_x,mouse_y = pygame.mouse.get_pos()
             if target_x < mouse_x < target_x + target_width and target_y< mouse_y < target_y + target_height:
                 target_x = random.randint(0, SCREEN_WIDTH - target_width)
                 target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    screen.fill(color)
    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

pygame.quit()
