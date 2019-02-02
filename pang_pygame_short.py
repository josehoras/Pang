import time
import pygame
from pygame.locals import *
import pygame.surfarray as surfarray
import matplotlib.pyplot as plt
import os
from pang_pygame_classes import *
from pang_pygame_game_functions import *

position = [1920+100, 100]

os.environ['SDL_VIDEO_WINDOW_POS'] = str(position[0]) + "," + str(position[1])
#os.environ['SDL_VIDEO_CENTERED'] = '1'

SCREEN_X = 550
SCREEN_Y = 700

#MAIN FUNCTION
pygame.init()
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))

player = Player(SCREEN_X/2, SCREEN_Y-40, SCREEN_X)
disparo = Shoot(SCREEN_Y)
ball_list = pygame.sprite.Group()

game_over = 0
#    for level in range(1, 3):
#        if game_over == 1: break


for level in range(3, 4):
    if game_over == 1: break
    disparo.destroy()
    player.rect.x = SCREEN_X/2
    player.xf = SCREEN_X/2
    generateLevel(SCREEN_X, SCREEN_Y, level, ball_list)
    update_screen(screen, player, disparo, ball_list)
    time.sleep(0.5)
    running = True
    while running:  
        running = not(check_quit_event())

        player.update(pygame.key.get_pressed()) 
        disparo.update(pygame.key.get_pressed(), player.rect.x)
        check_strike(disparo, ball_list, SCREEN_X, SCREEN_Y)
        
        if pygame.sprite.spritecollideany(player, ball_list):
            game_over = 1
            running = False
        if len(ball_list) == 0:
            print_banner("level", level)
            running = False      
        update_screen(screen, player, disparo, ball_list)
        
print_banner(screen, "over")
pygame.display.quit()

#screen_array = surfarray.array3d(screen)
#screen_array=np.transpose(screen_array, (1,0,2))
#plt.subplot(1, 1, 1)
#plt.imshow(screen_array)
#plt.axis('off')
#plt.show()
#disparo.update(pygame.key.get_pressed())