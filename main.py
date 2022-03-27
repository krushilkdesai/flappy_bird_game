print ("hello word")
from asyncio.windows_utils import pipe
from lib2to3.pytree import convert
import random
from re import T
import sys
from unicodedata import digit
from matplotlib import offsetbox
import pygame
from pygame.locals import*

FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY = SCREENHEIGHT*0.8
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


def isCollide (playerx,playery , upperPipes , lowerPipes):
    if plyery > GROUNDY - 25 or plyery < 0 :
        GAME_SOUNDS['chirp'].play()
        return True

    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if (plyery < pipeHeight + pipe ['y'] and abs[plyer - pipe ['x']]) < GAME_SPRITES ['pipe'][0].get_width():
            GAME_SOUND['chirp'].play()
            return True

    return False

def getRandomPIpe():
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT/3
    y2 =  offset + random.randrange (0,int (SCREENHEIGHT - GAME_SPRITES['base'].get_height() - 1.2 * offset))
    pipeX = SCREENWIDTH + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x':pipeX , "y": - y1},
        {'x':pipeX , "y": y2}
    ]
    return pipe

if _name_ == "_main_":
   pygame.init()
   FPSCLOCK = pygame.time.Clock()
   pygame.display.set_caption('Flappy Bird By Krushil K Desai')
   GAME_SPRITES['numbers']=(
       pygame.image.load('gallery/sprites/0.png').convert_alpha(),
       pygame.image.load('gallery/sprites/1.png').convert_alpha(),
       pygame.image.load('gallery/sprites/2.png').convert_alpha(),
       pygame.image.load('gallery/sprites/3.png').convert_alpha(),
       pygame.image.load('gallery/sprites/4.png').convert_alpha(),
       pygame.image.load('gallery/sprites/5.png').convert_alpha(),
       pygame.image.load('gallery/sprites/6.png').convert_alpha(),
       pygame.image.load('gallery/sprites/7.png').convert_alpha(),
       pygame.image.load('gallery/sprites/8.png').convert_alpha(),
       pygame.image.load('gallery/sprites/9.png').convert_alpha(),
   )

   GAME_SPRITES['message']=pygame.image.load('gallery/sprites/message.png').convert_alpha()
   GAME_SPRITES['base']=pygame.image.load('gallery/sprites/baes.png').convert_alpha()
   GAME_SPRITES['pipe']=(pygame.transform.ratate(pygame.image.load(PIPE).convert_alpha(),180),
   pygame.image.load(PIPE).convert_alpha()
   )

   GAME_SOUND['beat']=pygame.mixer.Sound('gallery/audio/beat.wav')
   GAME_SOUND['chirp']=pygame.mixer.Sound('gallery/audio/chirp.wav')
   GAME_SOUND['retro']=pygame.mixer.Sound('gallery/audio/retro.wav')
   GAME_SOUND['rocket']=pygame.mixer.Sound('gallery/audio/rocket.wav')
   GAME_SOUND['wind']=pygame.mixer.Sound('gallery/audio/wind.wav')

   GAME_SPRITES['blackground']=pygame.image.load(BACKGROUND).convert()
   GAME_SPRITES['player']=pygame.image.load(PLAYER).convert_alpha()


while True:
    welcomeScreen()
    MainGame()