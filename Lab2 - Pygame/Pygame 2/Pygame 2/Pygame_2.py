# -*- coding: utf-8 -*-
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)

    pygame.draw.circle(screen, BLACK, (WIDTH//2, HEIGHT//2), 200)

    square_size = 150
    x = WIDTH//2 - square_size//2
    y = HEIGHT//2 - square_size//2

    pygame.draw.rect(screen, YELLOW, (x, y, square_size, square_size))

    pygame.display.flip()
    clock.tick(60)
