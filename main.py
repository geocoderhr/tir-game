import pygame
import random


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HIGHT = 600
screen = pygame.display.set_mode((SCREEN_HIGHT,SCREEN_HIGHT))

pygame.display.set_caption("Игра Тир")

icon = pygame.image.load("img\img.png")
pygame.display.set_icon(icon)


target_img = pygame.image.load("img/09_49_34.png")
target_width = 80
target_height = 80
target_x = random.randint(0,SCREEN_WIDTH - target_width)
target_y = random.randint(0,SCREEN_HIGHT- target_width)


color =(random.randint(0,255),random.randint(0,255),random.randint(0,255))



pygame.display.set_mode()


runnig = True
while runnig:
    pass






pygame.quit()