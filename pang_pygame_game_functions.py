import pygame
from pygame.locals import *
from pang_pygame_classes import *
from random import randint

black = (0, 0, 0)
red = (255, 0, 0)
white= (255, 255, 255)
purple = (255, 0, 255)

#FUNCTIONS
def check_strike(disparo, ball_list, SCREEN_X, SCREEN_Y):
    for ball in ball_list:
        ball.update()
        if pygame.sprite.collide_rect(disparo, ball) == 1:
            if ball.rect.width > 20:
                nr = round(ball.rect.width / 4)
                nball1 = Ball(ball.rect.x, ball.rect.y, nr, 1, SCREEN_X, SCREEN_Y)
                nball2 = Ball(ball.rect.x, ball.rect.y, nr, -1, SCREEN_X, SCREEN_Y)
                ball_list.add(nball1)
                ball_list.add(nball2)
            ball_list.remove(ball)
            disparo.destroy()  

def print_banner(screen, status, level=0):
    if status == "over":
        txts = [("Game Over!", 72), ("Press ESC to quit", 30)]
        line = 0
        for txt in txts:
            font = pygame.font.SysFont("ubuntumono", txt[1])
            label = font.render(txt[0], True, (255,255,255))
            label_x = (screen.get_width() - font.size(txt[0])[0]) / 2
            label_y = (screen.get_height() - font.size(txt[0])[1]) / 2 + line * 80
            screen.blit(label, (label_x, label_y))
            line += 1
        pygame.display.flip()     
        while not(check_quit_event()):
            pass       
    if status == "level":
        txts = [("Level %i done!!!" % (level), 72), ("Press space to continue", 30)]
        line = 0
        for txt in txts:
            font = pygame.font.SysFont("ubuntumono", txt[1])
            label = font.render(txt[0] , True, (255,255,255))
            label_x = (screen.get_width() - font.size(txt[0])[0]) / 2
            label_y = (screen.get_height() - font.size(txt[0])[1]) / 2 + line * 80
            screen.blit(label, (label_x, label_y))
            line += 1
        pygame.display.flip()      
        while not(check_continue_event()) and not(check_quit_event()):
            pass
         
def update_screen(screen, player, disparo, ball_list):
    screen.fill(black)
    screen.blit(player.surf, player.rect)
    screen.blit(disparo.image, disparo.rect)
    for ball in ball_list:
      screen.blit(ball.image, ball.rect)
    pygame.display.flip()
        
def generateLevel(SCREEN_X, SCREEN_Y, levNumber, ball_list):
    for ball in ball_list: 
        ball_list.remove(ball)
        ball.kill()
    if levNumber == 1:
        balls_param = [[int(SCREEN_X/2)+80, int(SCREEN_Y/2)-30, 20, 1]]
    if levNumber == 2:
        balls_param = [[200, 250, 60, 1], [300, 250, 60, -1]]
    if levNumber == 3:
        balls_param = [[100, 300, 30, -1], [160, 300, 30, -1], [220, 300, 30, -1],
                [280, 300, 30, 1], [340, 300, 30, 1], [400, 300, 30, 1]]
    for param in balls_param:
        ball_list.add(Ball(param[0],param[1], param[2], param[3], SCREEN_X, SCREEN_Y))        


def check_quit_event():
    for event in pygame.event.get():
      if event.type == KEYDOWN and event.key == K_ESCAPE:
        return True
      elif event.type == QUIT:
        return True
    return False

def check_continue_event():
    for event in pygame.event.get():
      if event.type == KEYDOWN and event.key == K_SPACE:
        return True  