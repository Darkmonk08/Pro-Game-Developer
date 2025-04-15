class Bag:
    #class variables have same values as all objects
    brand="Nike"
    #instance variables
    #constructor
    def __init__(self,shape,size,color,material,):
        self.shape=shape
        self.size=size
        self.color=color
        self.material=material
        self.price=None
        
    def addprice(self,price):
        self.price=price
    def discount(self,percentage):
        self.price= self.price-(self.price*percentage/100)
#create objects
bag1=Bag("Rectangular","30feet", "blue", "Obsidian",)
print(bag1.brand)
print(bag1.shape)
print(bag1.color)
print(bag1.material)
print(bag1.size)
bag1.addprice(1000000)
print(bag1.price)
bag1.discount(30)
print(bag1.price)

bag2=Bag("circular","1 inch", "black", "water")
print(bag2.brand)
print(bag2.shape)
print(bag2.color)
print(bag2.material)
print(bag2.size)
print(bag2.price)