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

# Run game function
def runGame():
	#Set random start point
	startx = random.randint(5,CELLWIDTH - 6)
	starty = random.randint(5,CELLWIDTH - 6)
	womrCoords = [{'x':startx, 'y':starty},
		      {'x':startx - 1, 'y': starty},
		      {'x':startx - 2, 'y':starty}]
	direction = RIGHT

	#put food in a random place
	food = getRandomLocation()
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
			elif event.type = KEYDOWN:
				if(event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
					direction = LEFT
				elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
					direction = RIGHT
				elif(event.key == K_UP or event.key == K_w) and direction != DOWN:
					direction = UP
				elif(event.key == K_DOWN or event.key = K_s) and direction != UP:
					direction = DOWN
				elif event.key == K_ESCAPE:
					terminate()
		
		# heck if worm hit itself or and edge
		if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == CELLHEIGHT:
			return #game over
		for wormBody in wormCoords[1]:
			if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
				return #game over
		# Check if worm ate food
		if wormCoords[HEAD]['x'] == food['x'] and wormCoords[HEAD]['y'] == food['y']:
			# Dont remove worms tail segment
			food = getRandomLocation()
		else:
			del wormCoords[-1]# Remove worms tail segment
		
		# move worm
		if direction == UP:
			newHead = {'x':wormCoords[HEAD]['x'], 'y':wormCoords['y']-1}
		elif direction == DOWN:
			newHead = {'x':wormCoords[HEAD]['x'],'y':wormCoords[HEAD]['y']+1}
		elif direction == LEFT:
			newHead = {'x':wormCoords[HEAD]['x']-1,'y':wormCoords[HEAD]['y']}
		elif direction == RIGHT:
			newHead = {'x':wormCoords[HEAD]['x']+1,'y':wormCoords[HEAD]['y']}
		wormCoords.insert(0, newHead)

		#Draw Screen
		DISPLAYSURF.fill(BGCOLOR)
		drawGrid()
		drawWorm(wormCoords)
		drawFood(food)
		drawScore(len(wormCoords) - 3)
		pygame.display.update()
		FPSCLOCK.tick(FPS)
