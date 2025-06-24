import pygame

pygame.init()

WIDTH=1400
HEIGHT=800

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Invaders")

shipw=70
shiph=50
ship1x=20
ship1y=400
ship2x=1325
ship2y=400
speed=5
fps=60

ship1collision=pygame.USEREVENT+1
ship2collision=pygame.USEREVENT+2

font1=pygame.font.SysFont("Arial",63)
background=pygame.image.load(r"C:\Users\ragha\OneDrive\Desktop\Pro-Game Developer\spaceinvaders\images\background.jpg")
background=pygame.transform.scale(background,(WIDTH,HEIGHT))
ship1=pygame.image.load(r"C:\Users\ragha\OneDrive\Desktop\Pro-Game Developer\spaceinvaders\images\ship1.jpg")
ship1=pygame.transform.scale(ship1,(shipw,shiph))
ship1=pygame.transform.rotate(ship1,90)
ship2=pygame.image.load(r"C:\Users\ragha\OneDrive\Desktop\Pro-Game Developer\spaceinvaders\images\ship2.jpg")
ship2=pygame.transform.scale(ship2,(shipw,shiph))
ship2=pygame.transform.rotate(ship2,270)
divider=pygame.Rect(WIDTH/2-7,0,14,HEIGHT)
bullethitsound=pygame.mixer.Sound(r"C:\Users\ragha\OneDrive\Desktop\Pro-Game Developer\spaceinvaders\images\Grenade+1.mp3")
bulletfiresound=pygame.mixer.Sound(r"C:\Users\ragha\OneDrive\Desktop\Pro-Game Developer\spaceinvaders\images\Gun+Silencer.mp3")

def maingame():
    ship1rect=pygame.Rect(ship1x,ship1y,shipw,shiph)
    ship2rect=pygame.Rect(ship2x,ship2y,shipw,shiph)
    ship1health=100
    ship2health=100
    bulletship1=[]
    bulletship2=[]
    run=True
    clock=pygame.time.Clock()
    while run:
        clock.tick(fps)
        screen.blit(background,(0,0))
        screen.blit(ship1,(ship1rect.x,ship1rect.y))
        screen.blit(ship2,(ship2rect.x,ship2rect.y))
        text1=font1.render("Health:"+str(ship1health),True,(255,255,255))
        text2=font1.render("Health:"+str(ship2health),True,(255,255,255))
        screen.blit(text1,(10,10))
        screen.blit(text2,(1075,10))
        for bullet in bulletship1:
            pygame.draw.rect(screen,(255,0,0),bullet)
        for bullet in bulletship2:
            pygame.draw.rect(screen,(0,0,255),bullet)
        pygame.draw.rect(screen,(0,0,0),divider)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_e:
                    bullet=pygame.Rect(ship1rect.right,ship1rect.y+shiph/2,10,6)
                    bulletship1.append(bullet)
                    bulletfiresound.play()
                if event.key==pygame.K_u:
                    bullet=pygame.Rect(ship2rect.left,ship2rect.y+shiph/2,10,6)
                    bulletship2.append(bullet)
                    bulletfiresound.play()
            if event.type==ship2collision:
                ship2health=ship2health-10
                bullethitsound.play()
            if event.type==ship1collision:
                ship1health=ship1health-10
                bullethitsound.play()
        keys=pygame.key.get_pressed()   
        ship1movement(keys,ship1rect)
        ship2movement(keys,ship2rect)
        bulletmovement(ship1rect,ship2rect,bulletship1,bulletship2)
        winner=""
        if ship1health<=0:
            winner="ship2"
        if ship2health<=0:
            winner="ship1"
        if winner!="":
            text3=font1.render("Winner:"+str(winner),True,(255,255,255))
            screen.blit(text3,(550,HEIGHT/2))
            pygame.display.update()
            pygame.time.delay(6000)
            break
    maingame()       

def ship1movement(keyspressed,ship1rect):
    if keyspressed[pygame.K_w] and ship1rect.top>0:
        ship1rect.y=ship1rect.y-speed
    if keyspressed[pygame.K_s] and ship1rect.bottom<HEIGHT:
        ship1rect.y=ship1rect.y+speed
    if keyspressed[pygame.K_d] and ship1rect.right<divider.left:
        ship1rect.x=ship1rect.x+speed
    if keyspressed[pygame.K_a] and ship1rect.left>0:
        ship1rect.x=ship1rect.x-speed

def ship2movement(keyspressed,ship2rect):
    if keyspressed[pygame.K_i] and ship2rect.top>0:
        ship2rect.y=ship2rect.y-speed
    if keyspressed[pygame.K_k] and ship2rect.bottom<HEIGHT:
        ship2rect.y=ship2rect.y+speed
    if keyspressed[pygame.K_l] and ship2rect.right<=WIDTH:
        ship2rect.x=ship2rect.x+speed
    if keyspressed[pygame.K_j] and ship2rect.left>divider.right:
        ship2rect.x=ship2rect.x-speed


def bulletmovement(ship1rect,ship2rect,bulletship1,bulletship2):
    for bullet in bulletship1:
        bullet.x=bullet.x+5
        if bullet.x>=WIDTH:
            bulletship1.remove(bullet)
        if ship2rect.colliderect(bullet):
            pygame.event.post(pygame.event.Event(ship2collision))
            bulletship1.remove(bullet)
    for bullet in bulletship2:
        bullet.x=bullet.x-5
        if bullet.x<=0:
            bulletship2.remove(bullet)
        if ship1rect.colliderect(bullet):
            pygame.event.post(pygame.event.Event(ship1collision))
            bulletship2.remove(bullet)
    


    



maingame()

