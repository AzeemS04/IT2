import pygame
import math as m
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)


vindu_bredde= 800
vindu_hoyde=800

pygame.init()

vindu= pygame.display.set_mode([vindu_bredde,vindu_hoyde])

font = pygame.font.SysFont("Sora", 24)

fortsett = True




class Ball:
    def __init__(self,x,y,radius,farge,vindusobjekt):
        self.x=x
        self.y=y
        self.radius=radius
        self.farge=farge
        self.vindusobjekt=vindusobjekt

    def tegn(self):

        pygame.draw.circle(self.vindusobjekt,self.farge, (self.x,self.y), self.radius)

    def finnavstand(self,ball2):
        xAvstand2=(self.x - ball2.x)**2
        yAvstand2=(self.y - ball2.y)**2
        sentrumAvstand=m.sqrt(xAvstand2 + yAvstand2)

        radiuser= self.radius + ball2.radius
        avstand= sentrumAvstand -radiuser

        return avstand

class Hinder(Ball):
    def __init__(self, x, y, radius, farge, vindusobjekt,xFart, yFart):
        super().__init__(x, y, radius, farge, vindusobjekt)
        self.xFart = xFart
        self.yFart = yFart
    
    def flytt(self):
        if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.vindusobjekt.get_width()):
            self.xFart = -self.xFart
        if ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.vindusobjekt.get_height()):
            self.yFart = -self.yFart

        self.x += self.xFart
        self.y += self.yFart

class Spiller(Ball):
    def __init__(self, x, y,radius, farge, vindusobjekt,fart):
        super().__init__(x, y,radius, farge, vindusobjekt)
        self.fart=fart

    def flytt(self,taster):
        if taster[K_UP]:
            self.y -= self.fart
        if taster[K_DOWN]:
            self.y += self.fart
        if taster[K_LEFT]:
            self.x -= self.fart
        if taster[K_RIGHT]:
            self.x += self.fart

# ball = Ball(vindu_bredde/2,(vindu_hoyde/2), 2, 20,(149, 14, 27) ,vindu)

spiller1 = Spiller(200, 200, 20,(149, 14, 27),vindu,3)

hinder1 = Hinder(100, 100, 20, (0, 0, 255), vindu, 2.5, 1.5)

while fortsett:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fortsett = False



    trykkede_taster= pygame.key.get_pressed()

    vindu.fill((65, 39, 94))

    if trykkede_taster[K_UP]:
        bilde = font.render("Du trykker Pil opp!", True, (65, 62, 230))
        vindu.blit(bilde,(180,100))
    if trykkede_taster[K_DOWN]:
        bilde = font.render("Du trykker Pil ned!", True, (65, 62, 230))
        vindu.blit(bilde,(180,100))
    if trykkede_taster[K_LEFT]:
        bilde = font.render("Du trykker Pil venstre!", True, (65, 62, 230))
        vindu.blit(bilde,(180,100))
    if trykkede_taster[K_RIGHT]:
        bilde = font.render("Du trykker Pil høyre!", True, (65, 62, 230))
        vindu.blit(bilde,(180,100))


    spiller1.tegn()
    spiller1.flytt(trykkede_taster)
    hinder1.tegn()
    hinder1.flytt()

    print(spiller1.finnavstand(hinder1))

    pygame.display.flip()

pygame.quit()
 