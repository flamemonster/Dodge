import pygame
import setting
pygame.init()

screenwidth = 1280
screenheight = 1024

screen = pygame.display.set_mode((screenwidth,screenheight))
shopx= 640
shopy = 10
shopwidth = 80
shopheight = 30

shopb = pygame.Rect(shopx,shopy,shopwidth,shopheight)

black = (0,0,0)
yellow = (255,155,0)
white = (255,255,255)
font = pygame.font.SysFont("Arial",30)



def drawui():
    if setting.shop == True:
        item1 = font.render("1: increase player speed by 5  :$20",True,white)
        screen.blit(item1,(100,200))
        itemi = font.render(f"[{setting.pressed}/25]",True,white)
        screen.blit(itemi,(610,200))

def buyitem():
    setting.player_speed += 1
    setting.pressed += 1
    setting.coin -= 20
        
def shop():
    global pressed
    pygame.draw.rect(screen,yellow,shopb)
    shui = font.render("Shop",True,white)
    screen.blit(shui,(640,10))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        setting.shop = True
    if setting.shop == True:
        screen.fill(black)
    if keys[pygame.K_v]:
        setting.shop = False
    #if keys[pygame.K_1] and setting.shop == True:
        #if setting.coin >= 20:
            #setting.player_speed += 1
            #pressed += 1
            #setting.coin -= 20
