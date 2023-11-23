class point():
    def __init__(self ,x = 0,y = 0 ):
        self.x = x
        self.y = y

    def getx(self):
        return self.x
    
    def setx (self , x):
      self.x = x


    def distance (self,point):
        return (point.y - self. point) **2+ ((point.x - self .point)**2)**(1/2)
    

    def gety (self) :
        return self.y
    

    def sety (self , y):
      self.y = y


    def norme(self):
       n = (self.x**2 +self.y**2)**(1/2)
       return n
    
    def info(self):
       print(f"point x {self.x}:\npoint y{self.y}:\nnomre:{(self.x**2+self.y**2)**(1/2)}")
       point1=3
       point2=4
       point1.info()
       point2.info()
       pass