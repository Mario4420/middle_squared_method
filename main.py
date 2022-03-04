#!/usr/bin/python

import time
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

def middle_squared_method(seed: int, iterations: int):
    if seed % 2 != 0:
        seed += 1

    seed2 = str(seed**2).rjust(len(str(seed))*2, "0")
    if iterations != 0:
        return middle_squared_method(int(seed2[len(str(seed)) // 2 : len(seed2) - len(str(seed)) // 2]), iterations-1)
    else: 
        return int(seed2[len(str(seed)) // 2 : len(seed2) - len(str(seed)) // 2])

while True:
    x = (middle_squared_method(pygame.time.get_ticks(), 10)%600) + 1 
    y = (middle_squared_method(pygame.time.get_ticks(), 12)%600) + 1 
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), (x, y, 10, 10))

    pygame.display.update()
    
    if x != y:
        print(x, y)

    clock.tick(1)
