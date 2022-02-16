import random
import pygame
from pygame.locals import *

def position_radom():
    position_x = random.randint(0, 590)
    position_y = random.randint(0, 590)
    return(position_x//10*10, position_y//10*10)


def colission(player, object):  
    if (player[0] == object[0]) and (player[1] == object[1]):
        return True

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')




snake = [(200, 200), (210, 200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))



my_ditection = LEFT


apple = pygame.Surface((10,10))
apple_pos = position_radom()
apple.fill((255,0,0))

clock = pygame.time.Clock()
while True:
    clock.tick(16)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_ditection = UP
            if event.key == K_DOWN:
                my_ditection = DOWN
            if event.key == K_RIGHT:
                my_ditection = RIGHT
            if event.key == K_LEFT:
                my_ditection = LEFT



    if colission(snake[0], apple_pos):
        apple_pos = position_radom()
        snake.append((0,0))

    for i in range(len(snake)-1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])


    if my_ditection == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    elif my_ditection == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    elif my_ditection == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    elif my_ditection == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    

    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin,pos)





    pygame.display.update()        