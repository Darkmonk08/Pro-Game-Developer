import pygame

pygame.init()

WIDTH=1000
HEIGHT=800

screen=pygame.display.set_mode((WIDTH,HEIGHT))
run=True

image1=pygame.image.load("Image6.png")
image1=pygame.transform.scale(image1,(WIDTH,HEIGHT))
image2=pygame.image.load("Image7.png")
rocketx=500
rockety=400
moveup=False
movedown=True

while run==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run==False
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                moveup=True
                movedown=False
        if event.type==pygame.KEYUP:
            moveup=False
            movedown=True
    screen.blit(image1,(0,0))
    screen.blit(image2,(rocketx,rockety))
    if moveup:
        rockety=rockety-5
    if movedown:
        rockety=rockety+1

    pygame.display.update()
    