import pygame
import random
import time

pygame.init()

WIDTH=1000
HEIGHT=800

screen=pygame.display.set_mode((WIDTH,HEIGHT))
run=True
fps=60
clock=pygame.time.Clock()
score=0
font=pygame.font.SysFont("Arial",20)
font1=pygame.font.SysFont("Arial",100)
starttime=time.time()

background=pygame.image.load(r"C:\Users\ragha\OneDrive\Desktop\Jetlearn Python\Pro-Game-Developer\Sustainability-game\Images\Image_greenbg.png")
background=pygame.transform.scale(background,(WIDTH,HEIGHT))

class Bin(pygame.sprite.Sprite):
    def __init__(self,binx,biny):
        super().__init__()
        self.image=pygame.image.load(r"C:\Users\ragha\OneDrive\Desktop\Jetlearn Python\Pro-Game-Developer\Sustainability-game\Images\bin.png")
        self.image=pygame.transform.scale(self.image,(40,60))
        self.rect=self.image.get_rect()
        self.rect.center=(binx,biny)
    def update(self,keydown):
        if self.rect.y>=5 and keydown[pygame.K_w]:
            self.rect.y=self.rect.y-5
        if self.rect.y<=750 and keydown[pygame.K_s]:
            self.rect.y=self.rect.y+5
        if self.rect.x<=950 and keydown[pygame.K_d]:
            self.rect.x=self.rect.x+5
        if self.rect.x>=0 and keydown[pygame.K_a]:
            self.rect.x=self.rect.x-5



class Recyclable_objects(pygame.sprite.Sprite):
    recyclable_objects=["Image_box.png", "Image_pencil.png", "item1.png"]
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load(f"C:\\Users\\ragha\\OneDrive\\Desktop\\Jetlearn Python\\Pro-Game-Developer\\Sustainability-game\\Images\\{random.choice(self.recyclable_objects)}")
        self.image=pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(10,WIDTH-10),random.randint(10,HEIGHT-10))

class Nonrecyclable_objects(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load(r"C:\Users\ragha\OneDrive\Desktop\Jetlearn Python\Pro-Game-Developer\Sustainability-game\Images\Image_plasticbag.png")
        self.image=pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(10,WIDTH-10),random.randint(10,HEIGHT-10))

bins=pygame.sprite.Group()
bin=Bin(30,750)
bins.add(bin)

recyclables=pygame.sprite.Group()
for i in range(0,50):
    recyclable=Recyclable_objects()
    recyclables.add(recyclable)
    
nonrecyclables=pygame.sprite.Group()
for i in range(0,20):
    nonrecyclable=Nonrecyclable_objects()
    nonrecyclables.add(nonrecyclable)

while run==True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
    screen.blit(background,(0,0))
    timeelapsed=time.time() - starttime
    if timeelapsed>=30:
        if score>=35:
            youwin=font1.render("You Win",True,(0,0,0))
            screen.blit(youwin,(WIDTH/2,HEIGHT/2))
        else:
            youloose=font1.render("You Loose",True,(0,0,0))
            screen.blit(youloose,(WIDTH/2,HEIGHT/2))
    else:
        bins.draw(screen)
        keypressed=pygame.key.get_pressed()
        bins.update(keypressed)
        recyclables.draw(screen)
        nonrecyclables.draw(screen)
        binrecyclablecollision=pygame.sprite.spritecollide(bin,recyclables,dokill=True)
        binnonrecyclablecollision=pygame.sprite.spritecollide(bin,nonrecyclables,dokill=True)
        for i in binnonrecyclablecollision:
            score = score-1
        for i in binrecyclablecollision:
            score = score+1
        scoreblit=font.render("Score:"+str(score),True,(0,0,0))
        screen.blit(scoreblit,(0,0))
    

    pygame.display.update()
