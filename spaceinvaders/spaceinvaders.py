import pygame

pygame.init()

WIDTH=1400
HEIGHT=800

screen=pygame.display.set_mode((WIDTH,HEIGHT))

shipw=70
shiph=50
background=pygame.image.load(r"C:\Users\ragha\OneDrive\Desktop\Pro-Game Developer\spaceinvaders\images\background.jpg")
background=pygame.transform.scale(background,(WIDTH,HEIGHT))
ship1=pygame.image.load(r"C:\Users\ragha\OneDrive\Desktop\Pro-Game Developer\spaceinvaders\images\ship1.jpg")
ship1=pygame.transform.scale(ship1,(shipw,shiph))
ship2=pygame.image.load(r"C:\Users\ragha\OneDrive\Desktop\Pro-Game Developer\spaceinvaders\images\ship2.jpg")
ship2=pygame.transform.scale(ship2,(shipw,shiph))

run=True
while run:
    screen.blit(background,(0,0))
    screen.blit(ship1,(20,400))
    screen.blit(ship2,(1325,400))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()

