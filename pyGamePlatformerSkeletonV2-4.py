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
FPS = 120
FPSCLOCK = pygame.time.Clock()

# Setup global variables
backgroundColour = BLACK
gameOver = False
gameKeysPressed = set()

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)


# Setup classes

class Player(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([20, 20])
       self.image.fill(color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.rect.x = 100
       self.rect.y = 50

    def update(self):
        if "RIGHT" in gameKeysPressed:
            self.rect.x = self.rect.x + 1
            #self.rect.x += 1
            if pygame.sprite.spritecollideany(self, allPlatforms):
                self.rect.x = self.rect.x - 1
        if "LEFT" in gameKeysPressed:
            self.rect.x = self.rect.x - 1
            #self.rect.x -= 1
            if pygame.sprite.spritecollideany(self, allPlatforms):
                self.rect.x = self.rect.x + 1
        self.rect.y = self.rect.y + 1
        if pygame.sprite.spritecollideany(self, allPlatforms):
            self.rect.y = self.rect.y - 1

# Setup functions

def printVariablesToConsole():
    #global gameOver
    
    print(gameOver)
    print(gameKeysPressed)
    print(player.rect)
    
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

    player.update()

def updateBadSprites():
    pass

def updateGoodSprites():
    pass

def drawPlatforms():
    plat1 = pygame.sprite.Sprite()
    plat1.image = pygame.Surface([200, 20])
    plat1.image.fill(BLUE)

    # Fetch the rectangle object that has the dimensions of the image
    # Update the position of this object by setting the values of rect.x and rect.y
    plat1.rect = plat1.image.get_rect()
    plat1.rect.x = 100
    plat1.rect.y = 550
    allPlatforms.add(plat1)

    plat2 = pygame.sprite.Sprite()
    plat2.image = pygame.Surface([280, 20])
    plat2.image.fill(RED)

    # Fetch the rectangle object that has the dimensions of the image
    # Update the position of this object by setting the values of rect.x and rect.y
    plat2.rect = plat2.image.get_rect()
    plat2.rect.x = 190
    plat2.rect.y = 200
    allPlatforms.add(plat2)

    

def updateScreenOutput():
    global backgroundColour, player
    
    if "RED" in gameKeysPressed:
        backgroundColour = RED
    elif "GREEN" in gameKeysPressed:
        backgroundColour = GREEN
    elif "BLUE" in gameKeysPressed:
        backgroundColour = BLUE
    screen.fill(backgroundColour)
    screen.blit(player.image, player.rect)
    allPlatforms.draw(screen)
#    for badSprite in badSpriteGroup:
#        screen.blit(badSprite, badSpriteRect)
#    for goodSprite in goodSpriteGroup:
#        screen.blit(goodSprite, goodSpriteRect)
#    pygame.display.update()
    pygame.display.flip()

def checkGameOver():
    if "QUIT" in gameKeysPressed:
        return True
    if (player.rect.y > 600):
        return True
    return False

player = Player(GREEN,0,0)
allPlatforms = pygame.sprite.Group()

def main():
    # specify which global variables can be used in the main function
    global gameOver
    drawPlatforms()
    
    while not gameOver:
        #printVariablesToConsole() # for troubleshooting
        checkUserInput()
        updatePlayerSprite()
        #updateBadSprites()
        #updateGoodSprites()
        updateScreenOutput()
        gameOver = checkGameOver()
        #pygame.time.Clock[]
        #print(pygame.time.get_ticks())
        #FPSCLOCK.tick(FPS)
    print("Ending Game")
    printVariablesToConsole() # for troubleshooting

if __name__ == '__main__':
    main()
