print ("hello word")
import random
import sys
from unicodedata import digit
import pygame
from pygame.locals import*

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


    playerx = int(SCREENWIDTH/5)
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
    score = 0
    playerx = int (SCREENWIDTH/5)
    playery = int(SCREENWIDTH/2) 
    base = 0


    newPipe1 = getRamdomPipe() 
    newPipe2 = getRandomPipe()


    upperPipes = [
        {'x':SCREENWIDTH + 200 , 'y': newPipe1[0]['y']},
        {'x' : SCREENWIDTH + 200 + (SCREENWIDTH/2),'y':newPipe2[0]['y']},
]  


    lower= [
        {'x': SCRREENWIDTH + 200 ,'y':newPipe1[1]['y']},
        {'x':SCREENWIDTH+200+(SCRESNWIDTH/2),'y': newPipe2[1]['y']},
    ]

    pipeVelX = -4


    playerVelY = -9
    playerMaxvelY = 10
    playerMinVelY = -8
    playerAccY = 1

    playerFlapAccv = -8
    playerFlapped = False
    
    while True :
        for event in pygame.event.get():
            if event.type == Quit or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == KRYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0 :
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    GAME_SOUND['beat'].play()

        crashTest = isCollide (playerx,playery,upperPipes,lowerPipe)
        if crashTest :
            return


        playerMidPos = playerx + GAME_SPRITES['Player'].get_width()/2
        for pipr in upperPipes:
            pipeMidPos = Pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
            if pipeMidpos <= playerMidPos<pipeMidPos+4:
                score += 1
                print(f"Your score is {score}")
                GAME_SOUNDS['point'].play()


        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY


        if playerFlapped :
            playerFlapped = False
            playerHeigh = GAME_SPRITES['player'].get_height()
            playery = playery + min(playerVelY,GROUNDY-player-playerHeigh)
        
        for upperPipe , lowerPipe in zip (upperPipes , lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX
        

        if 0<upperPipes[0]['x']<5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPIpes.append(newpipe[1])

        if upperPipe [0]['x']- GAME_SPRITES['pipe'][0].get_width():
            upperpipes.pop(0)
            lowerpipes.pop(0)

        SCREEN.blit(GAME_SPRITES['blackgroun'] (0,0))
        for upperPipe,lowerPipe in zip (upperPipes,lowerPipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0],(upperpipe['x'],upperPipe['y']))        
            SCREEN.blit(GAME_SPRITES['pipe'],[1](lowerPipe['x'],lowerPipe['y']))


        SCREEN.blit(GAME_SPRITES['base'],(basex,GROUNDY))    
        SCREEN.blit(GAME_SPRITES['player'],(playerx,playery))
        myDigits = [int(x) for x in list (str(score))]
        width = 0
        for digit in mydigits:
            width += GAME_SPRITES['number'][digit].get_width()
            Xoffset = (SCREENWIDTH - width)/2


            for digit in mydigits:
                SCREEN.blit(GAME_SPRITES['numbers'][digit],(Xoffset,SCREENHEIGHT*0.12))
                Xoff += GAME_SPRITES ['numbers'][digit].get_width()



        pygame.display.update()
        FPSCLOCK.tick(FPS)


def isCollide ()    