class Person():
    def __init__(self,x,y,status):
        import random as rn
        self.x = x
        self.y = y
        if(status <= 1):
            if(rn.random() <=0.5):
                self.status = "carrier"
            else:
                self.status = "ill"
        else:
            self.status = "healthy"
        self.maxDistance = 1.0
        self.maxIllDistance = 0.1
    def move(self):
        import random
        import math    
        if (self.status == "ill"):
            dx = (random.random()*2 - 1)*self.maxIllDistance
            dy = (random.random()*2 -1)*math.sqrt(self.maxIllDistance**2 - dx**2)
            self.x = self.x + dx
            self.y = self.y + dy
        else:
            dx = (random.random()*2 - 1)*self.maxDistance
            dy = (random.random()*2 - 1)*math.sqrt(self.maxDistance**2 - dx**2)
            self.x = self.x + dx
            self.y = self.y + dy
    def distancesq(self,other):
        return (self.x - other.x)**2 + (self.y - other.y)**2
    def info(self):
        return f"Stan zdrowia: {self.status}\nPołożenie: (x,y) = ({self.x},{self.y})"
    def __str__(self):
        return self.info()        

class Population():
    infectionProbability = 0.2
    infectionDistance = 1
    people = []
    def __init__(self, w, h, liczba):
        import random as rn
        self.people.extend([Person(rn.random() * w, rn.random() * h, rn.random()/self.infectionProbability) for i in range(liczba)])
        self.h = h
        self.w = w
    def move(self):
        import random as rn
        for i in range(len(self.people)):
            self.people[i].move()
            if(self.people[i].x > self.w):
                self.people[i].x = self.people[i].x-100
            if(self.people[i].y > self.h):
                self.people[i].y = self.people[i].y-100
            if(self.people[i].x <0):
                self.people[i].x = self.people[i].x+100
            if(self.people[i].y <0):
                self.people[i].y = self.people[i].y+100
        for persn in self.people:
            if(persn.status =="ill" or persn.status =="carrier"):
                for a in (i for i in self.people if i.status == "healthy"):
                    if(persn.distancesq(a) <= self.infectionDistance**2):
                        if(rn.random()<=0.5):
                            a.status = "ill"
        
    def paint(self):
        import matplotlib.pyplot as plt
        from math import sin, pi
        from matplotlib.animation import FuncAnimation
        l = len(self.people)

        fig = plt.figure()
        ax = plt.axes(xlim=(0, self.w), ylim=(0, self.h))
        lines = [ax.plot([], [], ".",color="#D00000")[0], ax.plot([], [], ".",color="#7BC950")[0], ax.plot([], [], ".",color="#FFBA08")[0]]
        def init():
            return lines
        def update(frame):
            illx, illy, healx, healy, carx, cary = [],[],[],[],[],[]
            for i in range(l):
                if(self.people[i].status == "ill"):
                    illx.append(self.people[i].x)
                    illy.append(self.people[i].y)
                if(self.people[i].status == "carrier"):
                    carx.append(self.people[i].x)
                    cary.append(self.people[i].y)
                if(self.people[i].status == "healthy"):
                    healx.append(self.people[i].x)
                    healy.append(self.people[i].y)
            lines[0].set_data(illx, illy)
            lines[1].set_data(healx,healy)
            lines[2].set_data(carx,cary)
            self.move()
            return lines
        anim = FuncAnimation(fig, update, init_func=init,
                               frames=None,repeat=False)

        plt.show(block = True) 
    def info(self):
        ret = ""
        for i in range(len(self.people)):
            ret = ret + str(self.people[i]) + "\n"
        return ret[:-2]
    def __str__(self):
        return str(self.info())

a = Population(100,100,100)
a.paint()
