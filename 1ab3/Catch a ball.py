import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 2
x_end = 1200
y_end = 900
screen = pygame.display.set_mode((x_end, y_end))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

x = int()
y = int()
r = int()



def new_ball(x, y, r):
    '''рисует новый шарик '''
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(20, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    return x, y, r

def ball_moving():
    ''' sharik dvigaetsya'''
    new_ball(x, y, r)
    pygame.display.update()

    pass



def click():
    global points, misses, x, y, r
    if ((y1 - y)**2 + (x1 - x)**2) <= r**2:
        points += 1
        y = -1000
    else:
        misses += 1



def points_display(points):
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render("Points: " + str(points),
                                False, (255, 255, 255))
    screen.blit(textsurface, (0, 0))
    textsurface = myfont.render('Misses:' + str(misses),
                                False, (255, 255, 255))
    screen.blit(textsurface, (0, 40))


points = 0
misses = 0
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            A = pygame.mouse.get_pos()
            x1, y1 = A[0], A[1]
            click()
    points_display(points)
    ball_moving()
    screen.fill(BLACK)

pygame.quit()
