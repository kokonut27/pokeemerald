import pygame
from pygame.locals import *
import os
import random
from replit import db

key_up = "\x1b[A"
key_down = "\x1b[B"
key_right = "\x1b[C"
key_left = "\x1b[D"

def pokeemerald():
  pygame.init()
  logo = pygame.image.load("media/logo.jpeg")
  pygame.display.set_icon(logo)
  screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
  FramePerSec = pygame.time.Clock()

  class Player(pygame.sprite.Sprite):
    def __init__(self):
      super().__init__()
      self.image = pygame.image.load("media/Player.png").convert()
      self.rect = self.image.get_rect()
      self.rect.center = (160, 520)
 
    def update(self):
      pressed_keys = pygame.key.get_pressed()
      x, y = screen.get_size()

      if pressed_keys[38]:
        self.rect.move(0, -5)
      if pressed_keys[40]:
        self.rect.move(0,5)
         
      if self.rect.left > 0:
        if pressed_keys[37]:
          self.rect.move(-5, 0)
      if self.rect.right < x:        
        if pressed_keys[39]:
          self.rect.move(5, 0)
 
    def draw(self, surface):
      surface.blit(self.image, self.rect)    
      

  running = True

  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
        exit()
    Player().update()
    Player().draw(screen)

    pygame.display.update()
    FramePerSec.tick(60)

if __name__ == "__main__":
  os.system("clear")
  pokeemerald()