import pygame
import random

pygame.init()

WIDTH=1000
HEIGHT=800

screen=pygame.display.set_mode((WIDTH,HEIGHT))
numberofwalls=40
wallscreated=0
run=True
wallwidth=50
wallheight=20

class Wall(pygame.sprite.Sprite):
    def __init__(self,wallx,wally,alignment):
        super().__init__()
        self.image=pygame.image.load(r"C:\Users\ragha\OneDrive\Desktop\Jetlearn Python\Pro-Game-Developer\Stealthediamond\Images\wall.jpeg")
        self.image=pygame.transform.scale(self.image,(wallwidth,wallheight))
        if alignment==1:
            self.image=pygame.transform.rotate(self.image,90)
        self.rect=self.image.get_rect()
        self.rect.topleft=(wallx,wally)
        
        

walls=pygame.sprite.Group()
while wallscreated<numberofwalls:
    alignment=random.randint(0,1)
    wallx=random.randint(0,WIDTH-wallwidth)
    wally=random.randint(0,HEIGHT-wallwidth)
    wall=Wall(wallx,wally,alignment)
    if pygame.sprite.spritecollideany(wall,walls):
        print("collision")
        continue
    walls.add(wall)
    wallscreated=wallscreated+1

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
    walls.draw(screen)
    pygame.display.update()








        