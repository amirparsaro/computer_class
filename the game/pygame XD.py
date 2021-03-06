# imports
import pygame
import random

pygame.init()

# variables
## main variables
disp = pygame.display.set_mode((900, 500))
done = False
disptype = "main"
comic = pygame.font.Font("fonts/comic.ttf", 20)

##disp "main" variables
back = pygame.image.load("images/background.png")
war_ico = pygame.image.load("images/sword.png")
war_ico = pygame.transform.scale(war_ico, (100, 100))
update_ico = pygame.image.load("images/upgrade.png")
update_ico = pygame.transform.scale(update_ico, (100, 100))
shop_ico = pygame.image.load("images/Shopcart.png")
shop_ico = pygame.transform.scale(shop_ico, (100, 100))
settings = pygame.image.load("images/setting.png")
settings = pygame.transform.scale(settings, (25, 25))
power = pygame.image.load("images/power.png")
power = pygame.transform.scale(power, (25, 25))
diamond = pygame.image.load("images/diamond.png")
diamond = pygame.transform.scale(diamond, (25, 25))
coin = pygame.image.load("images/coin.png")
coin = pygame.transform.scale(coin, (25, 25))
plus = pygame.image.load("images/plus-icon.png")
plus = pygame.transform.scale(plus, (25, 25))
play = pygame.image.load("images/play.png")
play = pygame.transform.scale(play, (100, 59))
arrowdown = pygame.image.load("images/arrow-down.png")
arrowdown = pygame.transform.scale(arrowdown, (25, 25))
wooden_back = pygame.image.load("images/wooden-back.png")
'''mouse_click = pygame.mixer.Sound("voices/mouse click.wav")'''

info_r = open("files/informations.txt", "r")
info_w = open("files/informations.txt", "a")
coins = 0
diamonds = 0
points = 0
tank = 1
line = info_r.readlines()
for i in range(len(line)):
    if line[i] == "coins :\n":
        coins = int(line[i + 1])
    elif line[i] == "diamonds :\n":
        diamonds = int(line[i + 1])
    elif line[i] == "points :\n":
        points = int(line[i + 1])
    elif line[i] == tank:
        tank = int(line[i + 1])

###
p_coin = comic.render(str(coins), True, (0, 0, 0))
p_diamond = comic.render(str(diamonds), True, (0, 0, 0))
p_point = comic.render(str(points), True, (0, 0, 0))

# main loop
while not done:

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            xm, ym = event.pos
            if disptype != "war":
                if 200 < xm < 300 and 400 < ym < 500:
                    disptype = "update"
                    #click.play()
                elif 580 < xm < 680 and 400 <ym < 500:
                    disptype = "shop"
                    #click.play()
                elif 390 < xm < 490 and 400 < ym < 500:
                    disptype = "main"
                    #click.play()
                elif 860 < xm < 960 and 2.5 < ym < 27.5:
                    disptype = "shop"
                elif 710 < xm < 810 and 2.5 < ym < 27.5:
                    disptype = "shop"
    # updates

    # draws
    ##type = main
    if disptype == "main":
        disp.fill((255, 255, 255))
        disp.blit(back, (0, 0))
        pygame.draw.rect(disp, (0, 140, 230), (0, 0, 900, 30))
        pygame.draw.rect(disp, (0, 140, 230), (0, 375, 900, 125))
        disp.blit(settings, (2.5, 2.5))
        disp.blit(power, (30, 2.5))
        disp.blit(diamond, (600, 2.5))
        disp.blit(coin, (750, 2.5))
        disp.blit(plus, (860, 2.5))
        disp.blit(plus, (710, 2.5))
        disp.blit(p_coin, (780, .5))
        disp.blit(p_diamond, (630, 1.5))
        disp.blit(war_ico, (390, 400))
        disp.blit(update_ico, (200, 400))
        disp.blit(shop_ico, (580, 400))
        disp.blit(play, (390, 300))
        disp.blit(arrowdown, (427.5, 375))
    elif disptype == "update":
        disp.fill((255, 255, 255))
        disp.blit(wooden_back , (0 , 0))
        pygame.draw.rect(disp, (0, 140, 230), (0, 0, 900, 30))
        pygame.draw.rect(disp, (0, 140, 230), (0, 375, 900, 125))
        disp.blit(settings, (2.5, 2.5))
        disp.blit(power, (30, 2.5))
        disp.blit(diamond, (600, 2.5))
        disp.blit(coin, (750, 2.5))
        disp.blit(plus, (860, 2.5))
        disp.blit(plus, (710, 2.5))
        disp.blit(p_coin, (780, .5))
        disp.blit(p_diamond, (630, 1.5))
        disp.blit(war_ico, (390, 400))
        disp.blit(update_ico, (200, 400))
        disp.blit(shop_ico, (580, 400))
        disp.blit(arrowdown, (235, 375))
    elif disptype == "shop":
        disp.fill((255,255,255))
        disp.blit(wooden_back , (0 , 0))
        disp.fill((255, 255, 255))
        disp.blit(wooden_back, (0, 0))
        pygame.draw.rect(disp, (0, 140, 230), (0, 0, 900, 30))
        pygame.draw.rect(disp, (0, 140, 230), (0, 375, 900, 125))
        disp.blit(settings, (2.5, 2.5))
        disp.blit(power, (30, 2.5))
        disp.blit(diamond, (600, 2.5))
        disp.blit(coin, (750, 2.5))
        disp.blit(plus, (860, 2.5))
        disp.blit(plus, (710, 2.5))
        disp.blit(p_coin, (780, .5))
        disp.blit(p_diamond, (630, 1.5))
        disp.blit(war_ico, (390, 400))
        disp.blit(update_ico, (200, 400))
        disp.blit(shop_ico, (580, 400))
        disp.blit(arrowdown, (615, 375))
    # ends
    pygame.display.update()
    pygame.time.Clock().tick(30)
info_r.close()
info_w.close()
pygame.quit()
