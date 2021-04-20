class Circle():
    def __init__(self,x,y,r):
        self.x = float(x)
        self.y = float(y)
        if(float(r)>=0):
            self.r = float(r)
        else:
            self.r = 0
    def circumference(self):
        import math
        return 2 * math.pi * self.r
    def intersection(self, other):
        import math
        d = math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
        if(d > (other.r + self.r)):
            return 0
        elif(d == (other.r + self.r) ):
            return 1
        elif(d < (other.r + self.r) and d > abs(other.r - self.r)):
            return 2
        elif(d == abs(other.r - self.r)):
            return 1
        elif(d < abs(other.r - self.r)):
            return 0
        return False

import sys
args = sys.argv[1:]
a = Circle(args[0],args[1],args[2])
b = Circle(args[3],args[4],args[5])
print("Liczba punktów wspólnych:",a.intersection(b))
