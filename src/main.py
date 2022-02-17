import pygame
import os
from replit import db

key_up = "\x1b[A"
key_down = "\x1b[B"
key_right = "\x1b[C"
key_left = "\x1b[D"

def pokeemerald():
  pygame.init()
  logo = pygame.image.load("media/logo.jpeg")
  pygame.display.set_icon(logo)
  pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

  running = True

  while running:
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
        exit()

if __name__ == "__main__":
  os.system("clear")
  pokeemerald()