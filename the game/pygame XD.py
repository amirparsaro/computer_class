#imports
import pygame
import random
pygame.init()

#variables
## main variables
disp = pygame.display.set_mode((900 , 500))
done = False
disptype = "main"

##disp "main" variables
settings = pygame.image.load("images/setting.png")
settings = pygame.transform.scale(settings , (25 , 25))
power = pygame.image.load("images/power.png")
power = pygame.transform.scale(power , (25 , 25))
diamond = pygame.image.load("images/diamond.png")
diamond = pygame.transform.scale(diamond , (25 , 25))
coin = pygame.image.load("images/coin.png")
coin = pygame.transform.scale(coin , (25 , 25))
plus = pygame.image.load("images/plus-icon.png")
plus = pygame.transform.scale(plus , (25 , 25))

#main loop
while not done:

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #updates

    #draws
    ##type = main
    if disptype == "main":
        disp.fill((255,255,255))
        pygame.draw.rect(disp , (239 , 222 , 184) , (0 , 0 , 900 , 30))
        disp.blit(settings ,(2.5 , 2.5))
        disp.blit(power ,(30 , 2.5))
        disp.blit(diamond , (600 , 2.5))
        disp.blit(coin , (750 , 2.5))
        disp.blit(plus , (860 , 2.5))
        disp.blit(plus , (710 , 2.5))
        
    #ends
    pygame.display.update()
    pygame.time.Clock().tick(30)
pygame.quit()
