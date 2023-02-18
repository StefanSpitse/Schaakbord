import pygame
import numpy as np

from stockfish import Stockfish

pygame.init()
window = pygame.display.set_mode([8 * 100, 8 * 100])
clock = pygame.time.Clock()

def Update():
    pass

def Draw():
    window.fill((100, 100, 100))
    even = (255, 255, 255)
    odd = (0, 0, 0)

    for y in range(7):
        if even == (255, 255, 255):
            odd = even
            even = (0, 0, 0)
        else:
            odd = even
            even = (255, 255, 255)

        for x in range(7):
            if x % 2 == 0:
                pygame.draw.rect(window, even, [x * 100 + 50, 50 + 100 * y, 100, 100])
            else:
                pygame.draw.rect(window, odd, [x * 100 + 50, 50 + 100 * y, 100, 100])

    pygame.display.update()


mainloop = True

while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False

    Update()
    Draw()
pygame.quit()
