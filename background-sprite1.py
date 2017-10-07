# background and sprite using pygame
import pygame, time
pygame.init()
screen = pygame.display.set_mode((800,600))
#screen = pygame.surface.Surface((800,600))
backgroundImage = pygame.image.load("background2.jpg")
sunImage =pygame.image.load("sun1.png")
#sunImage2 =pygame.image.load("sun2.png")
screen.blit(backgroundImage,(0,0))
screen.blit(sunImage,(0,0))
for x in range(1,200):
    screen.blit(backgroundImage,(0,0))
    screen.blit(sunImage,(x,0))
    #screen.blit(sunImage2,(60,60))
    pygame.display.flip()
    time.sleep(3)
