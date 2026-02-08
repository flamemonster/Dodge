import pygame
import random
import os
import time
import shop
import setting

pygame.init()

admin = False
score = 0
health = 100
enem_speed = 5
enem_speed2 = 2
coin = 0
con = True
rate = random.randint(500,1000)
rate2 = random.randint(500,1000)
maximum_health = 100
high_score = 0
pause = False
damage = 5
shopp = False
player_speed = 10


screenwidth = 1280
screenheight = 1024

pygame.time.get_ticks()
current_time = pygame.time.get_ticks()

if os.path.exists("highscore.txt"):
    with open("highscore.txt","r") as file:
        try:
            high_score = int(file.read())
        except:
            high_score = 0

restart_button = pygame.Rect(500,600,200,50)

red = (255,0,0)
redish = (100,0,0)
white=(255,255,255)
black=(0,0,0)
green = (0,255,0)
blue = (0,0,255)
orange = (255,200,0)
pink = (255, 192, 203)

text = ""
enter = ""
adminp = False
adminb = False

enemyy=[]
enemyx=[]

screen = pygame.display.set_mode((screenwidth,screenheight),pygame.FULLSCREEN)
pygame.display.set_caption("game")

font = pygame.font.SysFont("Arial",30)

for i in range(rate):
    enemies = pygame.Rect(random.randint(0,screenwidth-50),0,50,50)
    enemyy.append(enemies)

for i in range (rate2):
    enemies2 = pygame.Rect(0,random.randint(0,screenheight-50),50,50)
    enemyx.append(enemies2)
limit2x = screenwidth
limit2y = 0
limit2width = 50
limit2height = screenheight

limitx = 0
limity = screenheight
limitwidth = screenwidth
limitheight = 50

playerx = 640
playery = 700
playerwidth = 50
playerheight = 50


hbgx = 640
hbgy = 100
hbgwidth = maximum_health
hbgheight = 30
barx = 640
bary = 100
barwidth = 100
barheight = 30

menux = 350
menuy = 100
menuwidth = 510
menuheight = 900

god_mode = False
damage = 5
bar = pygame.Rect(barx,bary,barwidth,barheight)
limit = pygame.Rect(limitx,limity,limitwidth,limitheight)
limit2 = pygame.Rect(limit2x,limit2y,limit2width,limit2height)
player = pygame.Rect(playerx,playery,playerwidth,playerheight)

debuffwidth = 30
debuffx = random.randint(0,screenwidth-debuffwidth)
debuffy = 0
debuffheight = 30

debuff = pygame.Rect(debuffx,debuffy,debuffwidth,debuffheight)

        
def collider():
    #global coin
    global health
    global score
    if con == True:
        if pause == False:
            if god_mode == False:
                for e in enemyy:
                    if player.colliderect(e):
                        health -= damage
                        e.y = -50
                        e.x = random.randint(0,screenwidth-e.width)
                        bar.width -= damage
                for x in enemyx:
                    if player.colliderect(x):
                        health -= damage
                        x.y = random.randint(0,screenwidth-x.width)
                        x.x = -50
                        bar.width -= damage
            for y in enemyy:
                if y.colliderect(limit):
                    score += 1
                    y.y = -50
                    y.x = random.randint(0,screenwidth-y.width)
            for z in enemyx:
                if z.colliderect(limit2):
                    setting.coin += 1
                    z.y = random.randint(0,screenwidth-z.width)
                    z.x = -50
            if player.colliderect(debuff) and hdif > 5:
                health += 10
                bar.width += 10
                debuff.x = random.randint(0,screenwidth-debuff.width)
                debuff.y = 0
            if debuff.colliderect(limit):
                debuff.x = random.randint(0,screenwidth-debuff.width)
                debuff.y = 0
def movement():
    if con == True:
        if pause == False:
            if setting.shop == False:
                debuff.y +=3
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RIGHT]:
                    player.x += setting.player_speed
                if keys[pygame.K_LEFT]:
                    player.x -= setting.player_speed
                if keys[pygame.K_UP]:
                    player.y -= setting.player_speed
                if keys[pygame.K_DOWN]:
                    player.y += setting.player_speed
                for e in enemyy:
                    if admin == False:
                        e.y +=enem_speed
                        if e.x > player.x:
                            e.x -= enem_speed
                        elif e.x < player.x:
                            e.x += enem_speed
                if score >= 100:
                    for ex in enemyx:
                        if admin == False:
                            ex.x += enem_speed2
                            if ex.y > player.y:
                                ex.y -= enem_speed2
                            elif ex.y < player.y:
                                ex.y += enem_speed2

def spawn():
    if con == True and setting.shop == False:
        for e in enemyy:
            pygame.draw.rect(screen,red,e) 
        if score >= 100:
            for j in enemyx:
                pygame.draw.rect(screen,orange,j)
        pygame.draw.rect(screen,pink,debuff)


def draw_ui():
    cui = font.render(f"coins: {setting.coin}",True,white)
    screen.blit(cui,(20,60))
    if con == True and setting.shop == False:
        draw = font.render(f"score: {score}",True,white)
        screen.blit(draw,(20,20))
        pui = font.render(f"{percent}/{maximum_health}",True,blue)
        screen.blit(pui,(640,100))
        sui = font.render(f"Enemy speed:{enem_speed}",True,white)
        screen.blit(sui,(1050,20))
        hui = font.render(f"high score: {high_score}",True,white)
        screen.blit(hui,(1050,60))
def restart():
    global score,health,bar,enem_speed,enem_speed2,con
    score = 0
    health = 100
    bar.width = 100
    enem_speed = 5
    enem_speed2 = 2
    setting.coin = 0
    con = True
    spawn()
    setting.player_speed = 9
    setting.pressed=0
    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if setting.shop == True and setting.pressed < 25:
                if event.key == pygame.K_1:
                    shop.buyitem()
            if adminp == True:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif event.key == pygame.K_RETURN:
                    enter = text
                    text = ""
                else:
                    text += event.unicode
    if con == False and event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = event.pos
        if restart_button.collidepoint(mouse_pos):
            restart()
            
            
    screen.fill(black)
    #print(current_time)
    if con == True and setting.shop == False:
        pygame.draw.rect(screen,red,(hbgx,hbgy,hbgwidth,hbgheight))
        pygame.draw.rect(screen,green,bar)
        pygame.draw.rect(screen,white,limit)
        pygame.draw.rect(screen,white,player)
        pygame.draw.rect(screen,white,limit2)
        
        
    if health <= 0:
        con = False
        screen.fill(redish)
        healthb = font.render(f"GAME OVER",True,white)
        screen.blit(healthb,(500,512))
        draw = font.render(f"final score: {score}",True,white)
        screen.blit(draw,(500,700))
        restartt = font.render(f"Restart",True,white)
        pygame.draw.rect(screen,green,restart_button)
        screen.blit(restartt,(550,600))
        ghui=font.render(f"high score: {high_score}",True,white)
        screen.blit(ghui,(500,750))
        with open("highscore.txt","w") as file:
            file.write(str(high_score))
            
            
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        pause = True
        adminp = True
    percent = health
    how = damage/barwidth*100
    
    
    if score > high_score:
        high_score = score
    if player.x < 3:
        player.x = 3
    if player.x > screenwidth-playerwidth:
        player.x = screenwidth - playerwidth
    if player.y > screenheight-playerheight:
        player.y = screenheight-playerheight
    if player.y < 0:
        player.y = 0
        
        
    if con == True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            pause = True
        if keys[pygame.K_c]:
            pause = False
            setting.shop = False
    hdif = maximum_health - health
    print(enter)
    shop.shop()
    draw_ui()
    collider()
    movement()
    spawn()
    shop.drawui()
    
    
    if adminp == True:
        pygame.draw.rect(screen,orange,(menux,menuy,menuwidth,menuheight))
        fontt = pygame.font.SysFont("Arial",40)
        admp = fontt.render("enter the admin password",True,white)
        screen.blit(admp,(370,200))
        admt = fontt.render(text,True,black)
        screen.blit(admt,(350,300))
    if enter == "flame":
        adminb = True
    if adminb == True:
        pygame.draw.rect(screen,white,(menux,menuy,menuwidth,menuheight))
        aft = fontt.render("welcome to the admin block",True,black)
        screen.blit(aft,(370,200))
        admt = fontt.render(text,True,black)
        screen.blit(admt,(350,300))
        if enter == "cancel":
            running = False
        if enter == "admin quit":
            adminp = False
            adminb = False
            pause = False
        if enter == "infinit health":
            damage = 0
        if enter == "grinding":
            god_mode = True
            enem_speed = 10
            enem_speed2 = 10
        if enter == "ungrinding":
            god_mode = False
            enem_speed = 5
            enem_speed2 = 5
        if enter == "f":
            enem_speed = 100
            enem_speed2 = 100
        elif enter == "unf":
            enem_speed = 10
            enem_speed2 = 10
    pygame.display.flip()
pygame.quit()
    