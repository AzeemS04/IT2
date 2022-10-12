import random
import os
import sys, time

def slow_type(t):
    typing_speed = 50 #wpm
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)



class Spiller:
    def __init__(self,navn,helse,styrke):
        self.navn= navn
        self.helse= helse
        self.styrke= styrke
        

class Monster:
    def __init__(self,navn,helse,styrke,penger):
        self.navn= navn
        self.helse= helse
        self.styrke= styrke
        self.penger= penger


spiller1=Spiller("Azeem",100,50)

slow_type("Velkommen til Arena 1v1 \n")

while (True):
    break
