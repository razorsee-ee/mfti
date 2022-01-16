import pygame
from pygame.draw import *

pygame.init()

FPS = 30
end_x = 1234  # x coordinate of bottom right
end_y = end_x  # y coordinate of bottom right

screen = pygame.display.set_mode((end_x, end_y))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREY = (192, 192, 192)

screen.fill(GREY)


circle(screen, YELLOW, (end_x/2, end_y/2), end_x*0.35)      # face
rect(screen, BLACK, [end_x*0.33, end_y*0.65, end_x*0.33, end_y*0.05])   # mouth

circle(screen, RED, (end_x/3, end_y*0.45), end_x*0.08)   # right eye
circle(screen, BLACK, (end_x/3, end_y*0.45), end_x*0.08, 1)
circle(screen, BLACK, (end_x/3, end_y*0.45), end_x*0.03)

circle(screen, RED, (end_x/3*2, end_y*0.45), end_x*0.05)   # left eye
circle(screen, BLACK, (end_x/3*2, end_y*0.45), end_x*0.05, 1)
circle(screen, BLACK, (end_x/3*2, end_y*0.45), end_x*0.03)

line(screen, BLACK, (end_x*0.25, end_y*0.3), (end_x*0.42, end_y*0.4), int(end_x/70))    # right eyebrow
line(screen, BLACK, (end_x*0.6, end_y*0.4), (end_x*0.8, end_y*0.35), int(end_x/70))    # left eyebrow

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
