# -*- coding: utf-8 -*-
import pygame
import sys

pygame.init()

width = 600
height = 600
screen = pygame.display.set_mode((width, height))

CZARNY = (0, 0, 0)
ZIELONY = (0, 255, 0)

try:
    original = pygame.image.load("zdjecie.png").convert()
    original.set_colorkey(ZIELONY)
    img = pygame.transform.scale(original, (300, 300))
except:
    img = pygame.Surface((300, 300))
    img.fill(ZIELONY)

mode = 0

def draw(image, x=None, y=None):
    screen.fill(CZARNY)
    if x is None:
        x = (width - image.get_width()) // 2
    if y is None:
        y = (height - image.get_height()) // 2
    screen.blit(image, (x, y))
    pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if pygame.K_1 <= event.key <= pygame.K_9:
                mode = event.key - pygame.K_0

    shape = img

    if mode == 1:
        shape = pygame.transform.scale(img, (int(width * 0.2), int(height * 0.2)))

    elif mode == 2:
        shape = pygame.transform.rotate(img, -45)

    elif mode == 3:
        shape = pygame.transform.flip(img, False, True)

    elif mode == 4:
        a = pygame.transform.scale(img, (int(width * 0.7), height))
        shape = pygame.transform.rotozoom(a, 45, 0.7)

    elif mode == 5:
        shape = pygame.transform.scale(img, (int(width * 0.9), int(height * 0.35)))
        draw(shape, 0, 1)
        continue

    elif mode == 6:
        shape = pygame.transform.rotozoom(img, 270, 1)

    elif mode == 7:
        a = pygame.transform.scale(img, (int(img.get_width() * 0.7), img.get_height()))
        shape = pygame.transform.rotate(a, 180)

    elif mode == 8:
        a = pygame.transform.scale(img, (int(img.get_width() * 1.2), int(img.get_height() * 0.7)))
        shape = pygame.transform.rotate(a, -20)

    elif mode == 9:
        shape = pygame.transform.rotozoom(img, 180, 1)
        x = width - shape.get_width()
        y = (height - shape.get_height()) // 2
        draw(shape, x, y)
        continue

    draw(shape)

pygame.quit()
sys.exit()