import pygame
import math as m
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)

vindu_bredde= 1000
vindu_hoyde= 650

pygame.init()

vindu= pygame.display.set_mode([vindu_bredde,vindu_hoyde])

font = pygame.font.SysFont("Sora", 24)

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()


class Kule:
    def __init__(self,x,y,radius,farge,vindusobjekt):
        self.x=x
        self.y=y
        self.radius=radius
        self.farge=farge
        self.vindusobjekt=vindusobjekt

    def tegn(self):
        pygame.draw.circle(self.vindusobjekt,self.farge,(self.x,self.y),self.radius)





class Ball(Kule):
    def __init__(self, x, y, radius, farge, vindusobjekt,xFart,yFart):
        super().__init__(x, y, radius, farge, vindusobjekt)
        self.xFart=xFart
        self.yFart=yFart

    def flytt(self):
        if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.vindusobjekt.get_width()):
            self.xFart = -self.xFart
        if ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.vindusobjekt.get_height()):
            self.yFart = -self.yFart

        

        self.x += self.xFart
        self.y += self.yFart

class Padde:
    def __init__(self,x1,y1,x2,y2,farge,vindusobjekt,fart,tykkelse):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.farge=farge
        self.vindusobjekt=vindusobjekt
        self.fart=fart
        self.tykkelse=tykkelse

    def tegn(self):
        pygame.draw.line(self.vindusobjekt,self.farge,(self.x1,self.y1),(self.x2,self.y2),self.tykkelse)
'''
    def flytt(self,taster):
        if taster[K_UP]:
            if self.y1<=0:
                self.y1=0
                self.y2=200
            else:
                self.y1 -= self.fart
                self.y2 -= self.fart
        if taster[K_DOWN]:
            if self.y1>=450:
                self.y1=450
                self.y2=650
            else:
                self.y1 += self.fart
                self.y2 += self.fart
'''



ball1 = Ball(100, 100, 20, (0, 0, 255), vindu, 3.5, 4.5)
padde1= Padde()
padde2= Padde()

fortsett=True

while fortsett:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fortsett = False



    trykkede_taster= pygame.key.get_pressed()

    vindu.fill((65, 39, 94))

    ball1.tegn()
    ball1.flytt()

    pygame.display.flip()
    fpsClock.tick(FPS)

pygame.quit()
 