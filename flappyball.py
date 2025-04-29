import pgzrun

WIDTH=800
HEIGHT=600

class ball:
    GRAVITY=2000
    def __init__(self,color,size,startx,starty):
        self.color=color
        self.size=size
        self.x=startx
        self.y=starty
        self.yvelocity=0
        self.xvelocity=150
        
    def draw(self):
        screen.draw.filled_circle((self.x,self.y),self.size,self.color)

ball1=ball("orange",40,700,20)


def draw():
    screen.clear()
    screen.fill("black")
    ball1.draw()

def update(dt):
    initialvelocity=ball1.yvelocity
    ball1.yvelocity=initialvelocity+ball1.GRAVITY*dt #v=u+at
    s=(initialvelocity+ball1.yvelocity)/2*dt
    ball1.y=ball1.y+s
    if ball1.y>=HEIGHT:
        ball1.yvelocity=ball1.yvelocity*-0.89
    o=ball1.xvelocity*dt
    ball1.x=ball1.x+o
    if ball1.x>=WIDTH-ball1.size or ball1.x<=ball1.size:
        ball1.xvelocity=ball1.xvelocity*-0.89
        
def on_key_down(key):
    if key==keys.SPACE:
        ball1.yvelocity=-500





pgzrun.go()
