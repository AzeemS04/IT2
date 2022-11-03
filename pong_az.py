import pygame
import math as m
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)


vindu_bredde= 800
vindu_hoyde=800

pygame.init()

vindu= pygame.display.set_mode([vindu_bredde,vindu_hoyde])

font = pygame.font.SysFont("Sora", 24)

    

# def finnavstand(self,ball2):
#     xAvstand2=(self.x - ball2.x)**2
#     yAvstand2=(self.y - ball2.y)**2
#     sentrumAvstand=m.sqrt(xAvstand2 + yAvstand2)

#     radiuser= self.radius + ball2.radius
#     avstand= sentrumAvstand -radiuser

#     return avstand


class Ball:
    def __init__(self,x,y,radius,farge,vindusobjekt):
        self.x=x
        self.y=y
        self.radius=radius
        self.farge=farge
        self.vindusobjekt=vindusobjekt

    def tegn(self):
        pygame.draw.circle(self.vindusobjekt,self.farge,(self.x,self.y),self.radius)


class Hinder(Ball):
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


class Spiller:
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

    def flytt(self,taster):
        if taster[K_LEFT]:
            self.x1 -= self.fart
            self.x2 -= self.fart
        if taster[K_RIGHT]:
            self.x1 += self.fart
            self.x2 += self.fart
            

        

hinder1 = Hinder(100, 100, 20, (0, 0, 255), vindu, 2.5, 1.5)

spiller1=Spiller(300,600,500,600,(255,255,255),vindu,2,5)

fortsett=True

while fortsett:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fortsett = False



    trykkede_taster= pygame.key.get_pressed()

    vindu.fill((65, 39, 94))

    hinder1.tegn()
    hinder1.flytt()
    spiller1.tegn()
    spiller1.flytt(trykkede_taster)

   # print(finnavstand(spiller1,hinder1))
    pygame.display.flip()

pygame.quit()
 