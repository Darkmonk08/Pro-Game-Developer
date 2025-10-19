import pygame
import random
import time

pygame.init()

WIDTH=1000
HEIGHT=800

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Steal the Diamond")
numberofwalls=50
wallscreated=0
run=True
wallwidth=70
wallheight=20
fps=30
clock=pygame.time.Clock()
numberofgaurds=3
font=pygame.font.SysFont("Ariel", 40)
text1=font.render("EXIT",True,(255,0,0))
game_over_text = font.render("Game Over!", True, (255, 0, 0))
starttime=time.time()

class Wall(pygame.sprite.Sprite):
    def __init__(self,wallx,wally,alignment):
        super().__init__()
        self.image=pygame.image.load(r"C:\Users\ragha\OneDrive\Desktop\Jetlearn Python\Pro-Game-Developer\Stealthediamond\Images\wall.jpeg")
        self.image=pygame.transform.scale(self.image,(wallwidth,wallheight))
        if alignment==1:
            self.image=pygame.transform.rotate(self.image,90)
        self.rect=self.image.get_rect()
        self.rect.topleft=(wallx,wally)

class Rober(pygame.sprite.Sprite):
    speed=5
    def __init__(self,roberx,robery):
        super().__init__()
        self.image=pygame.image.load(r"C:\Users\ragha\OneDrive\Desktop\Jetlearn Python\Pro-Game-Developer\Stealthediamond\Images\rober.png")
        self.image=pygame.transform.scale(self.image,(40,60))
        self.rect=self.image.get_rect()
        self.rect.center=(roberx,robery)
    def update(self,keydown):
        old_pos = self.getroberpos()
        if self.rect.y>=5 and keydown[pygame.K_w]:
            self.rect.y=self.rect.y-self.speed
        if self.rect.y<=750 and keydown[pygame.K_s]:
            self.rect.y=self.rect.y+self.speed
        if self.rect.x<=950 and keydown[pygame.K_d]:
            self.rect.x=self.rect.x+self.speed
        if self.rect.x>=0 and keydown[pygame.K_a]:
            self.rect.x=self.rect.x-self.speed

        if pygame.sprite.spritecollideany(self, walls):
            self.rect.x, self.rect.y = old_pos
            
    def getroberpos(self):
        return self.rect.x,self.rect.y


class Diamond(pygame.sprite.Sprite):
    def __init__(self,diamondx,diamondy):
        super().__init__()
        self.image=pygame.image.load(r"C:\Users\ragha\OneDrive\Desktop\Jetlearn Python\Pro-Game-Developer\Stealthediamond\Images\diamond.png")
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect=self.image.get_rect()
        self.rect.center=(diamondx,diamondy)
    def new_movement(self,newdiamondpos):
        self.rect.center=newdiamondpos

class Gaurd(pygame.sprite.Sprite):
    gaurdspeed=2
    def __init__(self,gaurdx,gaurdy):
        super().__init__()
        self.image=pygame.image.load(r"C:\Users\ragha\OneDrive\Desktop\Jetlearn Python\Pro-Game-Developer\Stealthediamond\Images\gaurd.png")
        self.image=pygame.transform.scale(self.image,(90,60))
        self.rect=self.image.get_rect()
        self.rect.center=(gaurdx,gaurdy)
        self.direction=1
    def update(self):
        self.rect.x=self.rect.x+self.gaurdspeed*self.direction
    def changedirection(self):
        self.direction=self.direction*-1
        self.image=pygame.transform.flip(self.image,True,False)



diamonds=pygame.sprite.Group()
diamond=Diamond(WIDTH/2,60)
diamonds.add(diamond)

robers=pygame.sprite.Group()
rober=Rober(30,750)
robers.add(rober)

gaurds=pygame.sprite.Group()
for i in range(0,numberofgaurds):
    gaurd=Gaurd(random.randint(10,WIDTH-10),random.randint(30,HEIGHT-100))
    gaurds.add(gaurd)



walls=pygame.sprite.Group()
while wallscreated<numberofwalls:
    alignment=random.randint(0,1)
    wallx=random.randint(0,WIDTH-wallwidth)
    wally=random.randint(0,HEIGHT-wallwidth)
    wall=Wall(wallx,wally,alignment)
    if pygame.sprite.spritecollideany(wall,walls) or pygame.sprite.spritecollideany(wall,diamonds) or pygame.sprite.spritecollideany(wall,robers):
        continue
    wallpos = pygame.math.Vector2(wall.rect.center)
    too_close = False
    for guard in gaurds:
        guardpos = pygame.math.Vector2(guard.rect.center)
        distance = wallpos.distance_to(guardpos)
        if distance < 100:
            too_close = True
    if too_close:
        continue
    walls.add(wall)
    wallscreated=wallscreated+1
    

while run:
    clock.tick(fps)
    timeelapsed=time.time() - starttime
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()

    # if timeelapsed>=30:
    #     print()
    #     # if :
    #     #     youwin=font.render("You Win",True,(0,0,0))
    #     #     screen.blit(youwin,(WIDTH/2,HEIGHT/2))
    #     # else:
    #     #     youloose=font.render("You Loose",True,(0,0,0))
    #     #     screen.blit(youloose,(WIDTH/2,HEIGHT/2))
    # else:
    
    screen.fill((0,0,0))
    walls.draw(screen)
    robers.draw(screen)
    keypressed=pygame.key.get_pressed()
    robers.update(keypressed)
    diamonds.draw(screen)
    gaurds.draw(screen)
    gaurds.update()
    if pygame.sprite.spritecollideany(rober, gaurds):
        screen.fill((0, 0, 0))
        screen.blit(game_over_text, (WIDTH//2, HEIGHT//2))
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
        exit()
    pygame.display.update()
    for gaurd in gaurds.sprites():
        if pygame.sprite.spritecollideany(gaurd,walls) or gaurd.rect.right>=WIDTH-10 or gaurd.rect.left<=10:
            gaurd.changedirection()
    if pygame.sprite.collide_rect(rober,diamond):
        print("diamond")
        roberpos=rober.getroberpos()
        diamond.new_movement(roberpos)
    screen.blit(text1,(WIDTH-90,HEIGHT-90))
    exitrect=text1.get_rect(topleft=(WIDTH-90,HEIGHT-90))
    if rober.rect.colliderect(exitrect) and diamond.rect.colliderect(exitrect):
        print("game over")

    pygame.display.update()








    
