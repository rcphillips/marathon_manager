import pygame
from pygame import *



## makes it easy to tweak our constants
FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
RUNSPEED = 8


# making the game look right. centering it around the frame.
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) /2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) /2)

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



############################
#      The Main Game Loop  #
############################
def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    while True: #main game loop
        DISPLAYSURF.fill(BGCOLOR)
        for event in pygame.event.get(): #event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def drinkWater():

def drawTimer():

def drawWaterMeter():

