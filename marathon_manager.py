import pygame
from pygame.locals import *

## makes it easy to tweak our constants
FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
SCREENWIDTH = 600
SCREENHEIGHT = 420
RUNSPEED = 8


# making the game look right. centering it around the frame.
XMARGIN = int((WINDOWWIDTH - SCREENWIDTH)/2)
YMARGIN = int((WINDOWHEIGHT - SCREENHEIGHT)/2)

# easy access to colors
GRAY = (100, 100, 100)
NAVY = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)

# graphics
BGCOLOR = BLUE
FRAMECOLOR = BLACK
GROUNDCOLOR = GREEN
GROUNDHEIGHT = (SCREENHEIGHT * .25)
RUNNERHEIGHT = 100
RUNNERWIDTH = 50
RUNNERSPEED = 30

############################
#      The Main Game Loop  #
############################
def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Marathon Manager")

    #music
    pygame.mixer.init()
    pygame.mixer.music.load("HeatleyBros - 8 Bit Spring.mp3")
    pygame.mixer.music.play(-1)

    #background image
    #bg = pygame.image.load(os.path.join('images', 'bg.png')).convert()
    bg = pygame.image.load('sonic_background.png').convert()
    bg = pygame.transform.scale(bg, (SCREENWIDTH, SCREENHEIGHT))
    bgX = 0+XMARGIN
    bgX2 = bg.get_width()+XMARGIN
    
    #player image
    runnerImg = pygame.image.load('running_guy.png')
    resized_runnerImg = pygame.transform.scale(runnerImg, (RUNNERWIDTH,RUNNERHEIGHT))
    runnerx = XMARGIN+40
    runnery = (YMARGIN+SCREENHEIGHT-GROUNDHEIGHT-RUNNERHEIGHT)
    direction = 'right'

    while True: #main game loop
## pygame-drawn background
#        DISPLAYSURF.fill(FRAMECOLOR)
#        pygame.draw.rect(DISPLAYSURF, BGCOLOR, (XMARGIN, YMARGIN, SCREENWIDTH, SCREENHEIGHT))
#        pygame.draw.rect(DISPLAYSURF, GROUNDCOLOR, 
#                         (XMARGIN, 
#                          (YMARGIN+SCREENHEIGHT-GROUNDHEIGHT), 
#                          SCREENWIDTH, 
#                          GROUNDHEIGHT))

## if you want the runner to move       
        #if direction == 'right':
        #    runnerx +=5
        #    if runnerx >= XMARGIN+SCREENWIDTH:
        #        runnerx = XMARGIN    

## moving the background
        bgX -= 1.4
        bgX2 -= 1.4

        if bgX < bg.get_width() * -1:
            bgX = bg.get_width()
        if bgX2 < bg.get_width() * -1:
            bgX2 = bg.get_width()

        DISPLAYSURF.blit(bg, (bgX, 0+YMARGIN))
        DISPLAYSURF.blit(bg, (bgX2,0+YMARGIN))

        DISPLAYSURF.blit(resized_runnerImg, (runnerx, runnery))

        pygame.draw.rect(DISPLAYSURF,BLACK,(0,0,WINDOWWIDTH,WINDOWHEIGHT), 20)

        #event handling loop
        for event in pygame.event.get(): 
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def drinkWater():
    None
def drawTimer():
    None
def drawWaterMeter():
    None


if __name__ == '__main__':
    main()


