import pygame

pygame.init()

WIDTH=800
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
run=True

image1=pygame.image.load("Image5.png")
image1=pygame.transform.scale(image1,(WIDTH,HEIGHT))
image2=pygame.image.load("Image4.png")
image2=pygame.transform.scale(image2,(WIDTH,HEIGHT))

while run==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            screen.blit(image1,(0,0))
            pygame.display.update()
        if event.type==pygame.MOUSEBUTTONUP:
            screen.blit(image2,(0,0))
            pygame.display.update()






pgzrun.go()