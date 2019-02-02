import pygame
from pygame.locals import *

black = (0, 0, 0)
red = (255, 0, 0)
white= (255, 255, 255)
purple = (255, 0, 255)

#CLASSES
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, SCREEN_X):
        super(Player, self).__init__()
        self.endscreen = SCREEN_X
        self.surf = pygame.Surface((30, 80))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=(x, y))
        self.xf = x
    def update(self, pressed_keys):
        if pressed_keys[K_LEFT] and self.rect.left > 0:
            self.xf = self.xf - 0.2
        if pressed_keys[K_RIGHT] and self.rect.right < self.endscreen:
            self.xf = self.xf + 0.2
        self.rect.x = round(self.xf) 

class Shoot(pygame.sprite.Sprite):        
    def __init__(self, SCREEN_Y):
        super(Shoot, self).__init__()
        self.topscreen = SCREEN_Y
        self.image = pygame.Surface((20, SCREEN_Y))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(0, 1200))
        self.yf = SCREEN_Y
        self.exists = False
    def update(self, pressed_keys, player_x):
        if pressed_keys[K_UP] and self.exists == False:
            self.rect = self.image.get_rect(center=(player_x+15, self.topscreen*1.5))
            self.exists = True
        if self.exists: 
            #self.rect.move_ip(0, -1)
            self.yf -= 0.25
            self.rect.y = self.yf
            if self.rect.top == 0: self.destroy()
    def destroy(self):
        self.__init__(self.topscreen)

class Ball(pygame.sprite.Sprite):
    def __init__(self,  x, y, r, d, SCREEN_X, SCREEN_Y):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.screenx = SCREEN_X
        self.screeny = SCREEN_Y
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface((r*2, r*2))
        self.image.fill(white)
        self.image.set_colorkey(white)
        pygame.draw.circle(self.image, (0, 155, 150), (r, r), r-1, 0)
        pygame.draw.circle(self.image, (0, 200, 10), (r, r), r, 1)        
        self.rect = self.image.get_rect(center=(x+r, y+r))
        self.x0 = x
        self.y0 = y
        self.xf = x
        self.yf = y
        self.a = 0.01 
        self.b = - 2 * self.a * x
        self.c = y - self.a * x**2 - self.b * x
        self.step = 0.1 * d       
    def update(self):
        self.bounce()
        self.xf += self.step
        self.yf += (2 * self.a * self.rect.x + self.b) * self.step
        self.rect.x = round(self.xf) 
        self.rect.y = round(self.yf) 
    def bounce(self):
        if self.rect.x > self.screenx - self.rect.width or self.rect.x < self.rect.width/2:
            self.step = - self.step
            self.mirrorParabola()
        if self.rect.y > self.screeny - self.rect.width:
            self.mirrorParabola()
    def mirrorParabola(self):
            self.x0 = 2 * self.rect.x - self.x0
            self.b = - 2 * self.a * self.x0
            self.c = self.y0 + self.a * self.x0**2
    def destroy(self):
      pass