import pygame
import random

pygame.init()

WIDTH=1000
HEIGHT=800

screen=pygame.display.set_mode((WIDTH,HEIGHT))
run=True

background=pygame.image.load("Image_greenbg.png")
background=pygame.transform.scale(background,(WIDTH,HEIGHT))

class Bin(pygame.sprite.Sprite):
    def __init__(self,binx,biny):
        super().__init__()
        self.image=pygame.image.load("bin.png")
        self.rect=self.image.get_rect()
        self.rect.center=(binx,biny)

bins=pygame.sprite.Group()
bin=Bin(150,100)
bins.add(bin)

while run==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
    screen.blit(background,(0,0))
    bins.draw(screen)
    

    pygame.display.update()