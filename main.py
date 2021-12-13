from copy import deepcopy

import pygame
from random import randint

from config import RES, FPS, HEIGHT, WIDTH, TILE, W, H
from methods import check_cell

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()


if __name__ == '__main__':
    next_field = [[0 for i in range(W)] for j in range(H)]
    current_field = [[randint(0, 1) for i in range(W)] for j in range(H)]

    while True:
        surface.fill(pygame.Color('black'))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        # grid
        [pygame.draw.line(surface, pygame.Color('dimgray'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, TILE)]
        [pygame.draw.line(surface, pygame.Color('dimgray'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, TILE)]

        # process life
        for x in range(1, W - 1):
            for y in range(1, H - 1):
                if current_field[y][x]:
                    pygame.draw.rect(
                        surface,
                        pygame.Color('forestgreen'),
                        (x * TILE + 2, y * TILE + 2, TILE - 2, TILE - 2)
                    )
                next_field[y][x] = check_cell(current_field, x, y)

        current_field = deepcopy(next_field)

        pygame.display.flip()
        clock.tick(FPS)
