import pygame
import random

pygame.init()

WIDTH=1000
HEIGHT=800

screen=pygame.display.set_mode((WIDTH,HEIGHT))
run=True
fps=60
clock=pygame.time.Clock()

background=pygame.image.load(r"Sustainability-game\Images\Image_greenbg.png")
background=pygame.transform.scale(background,(WIDTH,HEIGHT))

class Bin(pygame.sprite.Sprite):
    def __init__(self,binx,biny):
        super().__init__()
        self.image=pygame.image.load(r"Sustainability-game\Images\bin.png")
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
        

bins=pygame.sprite.Group()
bin=Bin(30,750)
bins.add(bin)

while run==True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
    screen.blit(background,(0,0))
    bins.draw(screen)
    keypressed=pygame.key.get_pressed()
    bins.update(keypressed)
    

    pygame.display.update()