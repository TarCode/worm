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


