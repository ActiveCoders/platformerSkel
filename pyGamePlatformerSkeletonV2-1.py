# Title : 
# Author : 
# Version : 
# Date : 
# Copyright : ActiveCoders.club
# Created using Python skeleton code available at ActiveCoders.club

# Import external functionality
import pygame, sys

# Setup global constants
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
SCREEN_SIZE = (800,600)

# Setup global variables
backgroundColour = BLACK
gameOver = False
gameKeysPressed = set()

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)


# Setup classes

# Setup functions

def printVariablesToConsole():
    #global gameOver
    
    print(gameOver)
    print(gameKeysPressed)
    
def checkUserInput():
    global gameKeysPressed

    gameKeysPressed.clear()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    keysPressed = pygame.key.get_pressed()
    if keysPressed[pygame.K_LEFT] == 1:
        gameKeysPressed.add("LEFT")
    if keysPressed[pygame.K_RIGHT] == 1:
        gameKeysPressed.add("RIGHT")
    if keysPressed[pygame.K_SPACE] == 1:
        gameKeysPressed.add("SPACE")
    if keysPressed[pygame.K_q] == 1:
        gameKeysPressed.add("QUIT")
    if keysPressed[pygame.K_r] == 1:
        gameKeysPressed.add("RED")
    if keysPressed[pygame.K_g] == 1:
        gameKeysPressed.add("GREEN")
    if keysPressed[pygame.K_b] == 1:
        gameKeysPressed.add("BLUE")
        
    #print(keysPressed)

def updatePlayerSprite():
    pass

def updateBadSprites():
    pass

def updateGoodSprites():
    pass

def updateScreenOutput():
    global backgroundColour
    
    if "RED" in gameKeysPressed:
        backgroundColour = RED
    elif "GREEN" in gameKeysPressed:
        backgroundColour = GREEN
    elif "BLUE" in gameKeysPressed:
        backgroundColour = BLUE
    screen.fill(backgroundColour)
    pygame.display.flip()

def checkGameOver():
    if "QUIT" in gameKeysPressed:
        return True
    return False

def main():
    # specify which global variables can be used in the main function
    global gameOver
    
    while not gameOver:
        printVariablesToConsole() # for troubleshooting
        checkUserInput()
        updatePlayerSprite()
        updateBadSprites()
        updateGoodSprites()
        updateScreenOutput()
        gameOver = checkGameOver()
    print("Ending Game")
    printVariablesToConsole() # for troubleshooting

if __name__ == '__main__':
    main()
