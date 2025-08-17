import pygame

pygame.init()

WIDTH=800
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
run=True

class Rocket(pygame.sprite.Sprite):
    def __init__(self,rocketx,rockety):
        super().__init__()
        self.image=pygame.image.load("Image7.png")
        self.rect=self.image.get_rect()
        self.rect.center=(rocketx,rockety)
    def update(self):
        self.rect.y=self.rect.y-3



image1=pygame.image.load("Image6.png")
image1=pygame.transform.scale(image1,(WIDTH,HEIGHT))

rockets=pygame.sprite.Group()
rocket1=Rocket(150,600)
rockets.add(rocket1)
rocket2=Rocket(400,300)
rockets.add(rocket2)

while run==True:
    screen.blit(image1,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
    rockets.draw(screen)
    rockets.update()
    pygame.display.update()
    



    
