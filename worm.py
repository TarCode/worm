#	Date: 		23/06/2015
#	Author:		TarCode
#	File:		worm.py
#	Description:	wormy game clone using pygame. From inventwithpython tutorial
#
#############################################################################

#	imports
import random, pygame, sys
from pygame.locals import *

FPS = 15
WINDOWHEIGHT = 800
WINDOWWIDTH = 600
CELLSIZE = 30
assert WINDOWWIDTH % CELLSIZE == 0, "Window height must be a multiple of cell size"
assert WINDOWHEIGHT % CELLSIZE == 0, "Window width must be a multiple of cell size"
CELLWIDTH = int(WINDOWWIDTH/CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT/CELLSIZE)

#	      R    G    B
WHITE 	  = (230, 230, 230)
BLACK 	  = ( 10,  10,  20)
RED   	  = (230,   0,   0)
GREEN 	  = (  0, 230,   0)
DARKGREEN = (  0, 130,   0)
DARKGRAY  = ( 30,  30,  30)

BGCOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0 #worms head

# main
def main():
	global FPSCLOCK, DISPLAYSURF, BASICFONT

	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	BASICFONT = pygame.font.Font('freesansbold.ttf', 20)
	pygame.display.set_caption('WORM')
	
	showStartScreen()
	while True:
		runGame()
		showGameOverScreen()


