print ("hello word")
import random
import sys
import pygame
from pygame.locals import

FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGH))
GROUNDY = SCREENEIGHT*0.8
GAME_SPRITES={}
GAME_SOUND = {}
PLAYER = 'gallery/sprites/bird.png'
BACKGROUND = 'gallery/sprites/background.png'
PIPE = 'gallery/sprites/pipe.png'


def welcome():
    """Show welcome images on the screen
    """


 playerx = int(SCREENSIDTH/5)
 playery = int ((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
massagex = int((SREENWIDTH - GAME_SPRITES['massage'].get_width())/2)
messagey = int(SCREENHEIGHT*0.13)
basex = 0


while True:
     for event in pygame.event.get():
         if event.type == QUIT or (evevnt.type==KEYDOWN and event.key == K_ESCAPE):
             pygame.quit()
             sys.exit()

             elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                 return
else:
    SCREEN.blit (GAME_SPRITES['backgroun'],(0,0))
    SCEEN.bilt(GAME_SPRITES['playe'],(playerx,playery))
    SCREEN.bilt(GAME_SPRITES['massage'],(messagex,messame))
    SCREEN.bilt(GAME_SPRITES['base'],(basex,GROUND))
    pygame.display.update()
    FPSCLOCK.tick (FPS)


def mainGame():   
