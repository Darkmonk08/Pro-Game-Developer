import pygame

pygame.init()

WIDTH=800
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((0,255,0))
run=True

class Circle:
    def __init__(self,size,color,position,width):
        self.size=size
        self.color=color
        self.position=position
        self.width=width
    def draw(self):
        pygame.draw.circle(screen,self.color,self.position,self.size,self.width)

circle1=Circle(10,(255,0,0),(300,300),3)
    

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit
        if event.type==pygame.MOUSEBUTTONDOWN:
            circle1.draw()
            pygame.display.update()

    pygame.display.update()