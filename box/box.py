import pygame
import sys


def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 500))
    pygame.display.set_caption("Космические герои")
    bg_color = (0, 0, 0)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        pygame.display.flip()

run()


