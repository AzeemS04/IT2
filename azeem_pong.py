import pygame
import math as m
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)

vindu_bredde= 1100
vindu_hoyde= 750

pygame.init()

vindu= pygame.display.set_mode([vindu_bredde,vindu_hoyde])

font = pygame.font.SysFont("Sora", 24)

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()


class Ball:
    def __init__(self,x,y,radius,farge,vindusobjekt):
        self.x=x
        self.y=y
        self.radius=radius
        self.farge=farge
        self.vindusobjekt=vindusobjekt

    def tegn(self):
        pygame.draw.circle(self.vindusobjekt,self.farge,(self.x,self.y),self.radius)

