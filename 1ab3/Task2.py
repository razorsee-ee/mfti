import pygame
from pygame.draw import *

pygame.init()

FPS = 30
end_x = 1000  # x coordinate of bottom right
end_y = end_x * 0.6  # y coordinate of bottom right

screen = pygame.display.set_mode((end_x, end_y))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
DARKGREEN = (0, 100, 0)
ROSE = (255, 229, 204)


screen.fill(ROSE)


def palm(x_upperblock, y_upperblock, width, height):
    rect(screen, DARKGREEN, [x_upperblock, y_upperblock, width, height])
    rect(screen, DARKGREEN, [x_upperblock, (y_upperblock + height + 0.1*height), width, height])
    line(screen, DARKGREEN, (x_upperblock * 1.05, y_upperblock * 0.93),
                            (x_upperblock * 1.1, y_upperblock * 0.5),
                            int(width * 0.8))
    line(screen, DARKGREEN, (x_upperblock * 1.1, y_upperblock * 0.4),
                            (x_upperblock * 1.2, y_upperblock * 0.1),
                            int(width * 0.5))

    def branch(x, y, w, h):
        arc(screen, DARKGREEN, [1.1 * x, y, 5 * w, 0.5 * h], 0.5 * 3.14, 3.14, 3)
        arc(screen, DARKGREEN, [0.65 * x, 0.2 * y, 5 * w, 0.5 * h], 2 * 3.14, 0.5 * 3.14, 3)

    branch(x_upperblock, y_upperblock, width, height)


palm(end_x*0.5, end_y*0.3, end_x*0.04, end_y*0.2)
palm(end_x*0.2, end_y*0.3, end_x*0.03, end_y*0.16)
palm(end_x*0.35, end_y*0.3, end_x*0.03, end_y*0.10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
