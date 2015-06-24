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
WINDOWHEIGHT = 600
WINDOWWIDTH = 1200
CELLSIZE = 30
assert WINDOWWIDTH % CELLSIZE == 0, "Window height must be a multiple of cell size"
assert WINDOWHEIGHT % CELLSIZE == 0, "Window width must be a multiple of cell size"
CELLWIDTH = int(WINDOWWIDTH/CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT/CELLSIZE)

#	      R    G    B
WHITE 	  = (190, 190, 190)
BLACK 	  = ( 10,  10,  15)
RED   	  = (190,   0,   0)
GREEN 	  = (  0, 190,   0)
DARKGREEN = (  0, 100,   0)
DARKGRAY  = ( 50,  50,  50)

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
	wormCoords = [{'x':startx, 'y':starty},
		      {'x':startx - 1, 'y': starty},
		      {'x':startx - 2, 'y':starty}]
	direction = RIGHT

	#put food in a random place
	food = getRandomLocation()
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
			elif event.type == KEYDOWN:
				if(event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
					direction = LEFT
				elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
					direction = RIGHT
				elif(event.key == K_UP or event.key == K_w) and direction != DOWN:
					direction = UP
				elif(event.key == K_DOWN or event.key == K_s) and direction != UP:
					direction = DOWN
				elif event.key == K_ESCAPE:
					terminate()
		
		# Check if worm hit itself or and edge
		if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == CELLHEIGHT:
			return #game over
		for wormBody in wormCoords[1:]:
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
			newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
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

# Draw "Press a Key" to screen
def drawPressKeyMsg():
	pressKeySurf = BASICFONT.render('PRESS A KEY TO PLAY', True, DARKGRAY)
	pressKeyRect = pressKeySurf.get_rect()
	pressKeyRect.topleft = (WINDOWWIDTH - 300, WINDOWHEIGHT - 50)
	DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

#Check for key press function
def checkForKeyPress():
	if len(pygame.event.get(QUIT))>0:
		terminate()
	
	keyUpEvents = pygame.event.get(KEYUP)
	if len(keyUpEvents) == 0:
		return None
	if keyUpEvents[0].key == K_ESCAPE:
		terminate()
	return keyUpEvents[0].key

#Start Screen
def showStartScreen():
	titleFont = pygame.font.Font('freesansbold.ttf',180)
	titleSurf1 = titleFont.render('WORM!', True, WHITE, DARKGREEN)
	titleSurf2 = titleFont.render('WORM!',True, GREEN)
	
	degrees1 = 0
	degrees2 = 0
	while True:
		DISPLAYSURF.fill(BGCOLOR)

		#Rotate start Screen	
		rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
		rotatedRect1 = rotatedSurf1.get_rect()
		rotatedRect1.center = (WINDOWWIDTH/2,WINDOWHEIGHT/2)
		DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)
		
		rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
		rotatedRect2 = rotatedSurf2.get_rect()
		rotatedRect2.center = (WINDOWWIDTH/2,WINDOWHEIGHT/2)
		DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)

		drawPressKeyMsg()

		if checkForKeyPress():
			pygame.event.get()
			return
		pygame.display.update() #clear event queue
		FPSCLOCK.tick(FPS)

		degrees1 +=3
		degrees2 +=7

#terminate function
def terminate():
	pygame.quit()
	sys.exit()

#Where food appears
def getRandomLocation():
	return {'x':random.randint(0, CELLWIDTH -1), 'y':random.randint(0, CELLHEIGHT-1)}

#Game over screens
def showGameOverScreen():
	gameOverFont = pygame.font.Font('freesansbold.ttf', 180)
	gameSurf = gameOverFont.render('GAME', True, WHITE)
	overSurf = gameOverFont.render('OVER', True, WHITE)
	gameRect = gameSurf.get_rect()
	overRect = overSurf.get_rect()
	gameRect.midtop = (WINDOWWIDTH/2,10)
	overRect.midtop = (WINDOWWIDTH/2,gameRect.height+10+25)

	DISPLAYSURF.blit(gameSurf, gameRect)
	DISPLAYSURF.blit(overSurf, overRect)
	drawPressKeyMsg()
	pygame.display.update()
	
	pygame.time.wait(500)
	checkForKeyPress()
	
	while True:
		if checkForKeyPress():
			pygame.event.get()
			return

#Draw Score
def drawScore(score):
	scoreSurf = BASICFONT.render('Score: %s' % (score), True, WHITE)
	scoreRect = scoreSurf.get_rect()
	scoreRect.topleft = (WINDOWWIDTH - 120, 10)
	DISPLAYSURF.blit(scoreSurf,scoreRect)

#Draw Worm
def drawWorm(wormCoords):
	for coord in (wormCoords):
		x = coord['x']*CELLSIZE
		y = coord['y']*CELLSIZE
		wormSegmentRect = pygame.Rect(x,y,CELLSIZE,CELLSIZE)
		pygame.draw.rect(DISPLAYSURF, DARKGREEN, wormSegmentRect)
		wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
		pygame.draw.rect(DISPLAYSURF, GREEN, wormInnerSegmentRect)

#Draw Food
def drawFood(coord):
	x = coord['x']*CELLSIZE
	y = coord['y']*CELLSIZE
	foodRect = pygame.Rect(x,y,CELLSIZE,CELLSIZE)
	pygame.draw.rect(DISPLAYSURF, RED, foodRect)

#Draw grid
def drawGrid():
	for x in range(0, WINDOWWIDTH, CELLSIZE):
		pygame.draw.line(DISPLAYSURF, DARKGRAY,(x,0),(x,WINDOWHEIGHT))
	for y in range(0, WINDOWHEIGHT, CELLSIZE):
		pygame.draw.line(DISPLAYSURF, DARKGRAY, (0,y),(WINDOWWIDTH,y))

#main
if __name__ == '__main__':
	main()
