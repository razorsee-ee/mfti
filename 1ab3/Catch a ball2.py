import pygame
from pygame.draw import *
from random import randint
pygame.init()


x_screen = 1200
y_screen = 900
FPS = 30
screen = pygame.display.set_mode((x_screen, y_screen))
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
x = randint(100, 900)
y = randint(100, 700)
dx = 10
dy = 10
r = randint(30, 60)
color = COLORS[randint(0, 5)]


def new_ball(x, y, r):
    circle(screen, color, (x, y), r)


def click():
    global x, y, n, dx, dy, A, color
    x1 = A[0]
    y1 = A[1]
    if ((x1 - x) ** 2 + (y1 - y) ** 2) ** 0.5 <= r:
        print('goal')
        n += 1
    else:
        print('miss')
    color = COLORS[randint(0, 5)]
    x = randint(100, 900)
    y = randint(100, 700)
    dx *= -1 or 1
    dy *= -1 or 1


def new_position():
    global x, y, dx, dy, r
    x += dx
    y += dy
    if x >= x_screen - r or x < r:
        dx *= -1
    if y >= y_screen - r or y < r:
        dy *= -1



pygame.display.update()
clock = pygame.time.Clock()
finished = False
A = []
n = 0

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            A = pygame.mouse.get_pos()
            click()
    new_position()
    new_ball(x, y, r)
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()
print('Количество очков', n)
