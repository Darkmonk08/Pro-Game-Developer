import pygame
import time

pygame.init()

WIDTH=1000
HEIGHT=800
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Happy birthday")
run=True

image1=pygame.image.load("Image1.jpg")
image1=pygame.transform.scale(image1,(WIDTH,HEIGHT))
image2=pygame.image.load("Image2.jpg")
image2=pygame.transform.scale(image2,(WIDTH,HEIGHT))
image3=pygame.image.load("Image3.jpg")
image3=pygame.transform.scale(image3,(WIDTH,HEIGHT))

font1=pygame.font.SysFont("Arial",63)
text1=font1.render("Happy Birthday", True, (255,0,0))
text2=font1.render("Have fun", True, (0,255,0))
while run==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
    screen.blit(image1,(0,0))
    screen.blit(text1,(500,400))
    pygame.display.update()
    time.sleep(3)   
    screen.blit(image2,(0,0))
    screen.blit(text2,(300,200))
    pygame.display.update()
    time.sleep(3)
    screen.blit(image3,(0,0))
    pygame.display.update()
    time.sleep(3)

    





