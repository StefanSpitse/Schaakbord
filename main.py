import pygame

import numpy as np

pygame.init()
window = pygame.display.set_mode([9 * 100, 9 * 100])
clock = pygame.time.Clock()



board = [[["BR1"], ["BN1"], ["BB1"], ["BK"], ["BQ"], ["BB2"], ["BN2"], ["BR2"]],
         [["BP1"], ["BP2"], ["BP3"], ["BP4"], ["BP5"], ["BP6"], ["BP7"], ["BP8"]],
         [[""], [""], [""], [""], [""], [""], [""], [""]],
         [[""], [""], [""], [""], [""], [""], [""], [""]],
         [[""], [""], [""], [""], [""], [""], [""], [""]],
         [[""], [""], [""], [""], [""], [""], [""], [""]],
         [["WP1"], ["WP2"], ["WP3"], ["WP4"], ["WP5"], ["WP6"], ["WP7"], ["WP8"]],
         [["WR1"], ["WN1"], ["WB1"], ["WK"], ["WQ"], ["WB2"], ["WN2"], ["WR2"]]]


def Draw():
    window.fill((100, 100, 100))
    even = (255, 255, 255)
    odd = (0, 0, 0)
    count = 0
    for y in range(8):
        count = count + 1
        if even == (255, 255, 255):
            odd = even
            even = (0, 0, 0)

        else:
            odd = even
            even = (255, 255, 255)

        for x in range(8):
            if x % 2 == 0:

                pygame.draw.rect(window, even, [x * 100 + 50, 50 + 100 * y, 100, 100])

            else:

                pygame.draw.rect(window, odd, [x * 100 + 50, 50 + 100 * y, 100, 100])

    pygame.display.update()


pieces = []
mainloop = True

while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False

    if pygame.mouse.get_pressed()[0] == 1:
        print(board[round((pygame.mouse.get_pos()[1] / 5) / 20) - 1][round((pygame.mouse.get_pos()[0] / 5) / 20) - 1])
    Draw()
pygame.quit()
