import pygame

pygame.init()

WIDTH=1000
HEIGHT=800
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
    def growcircle(self):
        self.size=self.size+20

circle1=Circle(10,(255,0,0),(300,300),3)
circle2=Circle(30,(0,0,255), (250,150),8)
circle3=Circle(60,(150,3,169),(500,450),11)
circle4=Circle(90,(67,32,99),(900,700), 6)

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            circle1.draw()
            circle2.draw()
            circle3.draw()
            circle4.draw()
            pygame.display.update()
        if event.type==pygame.MOUSEBUTTONUP:
            circle1.growcircle()
            circle2.growcircle()
            circle3.growcircle()
            circle4.growcircle()
            pygame.display.update()
        if event.type==pygame.MOUSEMOTION:
            mousepos=pygame.mouse.get_pos()
            circle5=Circle(5,(0,0,0),mousepos,5)
            circle5.draw()
            pygame.display.update()
    pygame.display.update()
