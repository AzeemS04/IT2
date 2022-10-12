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
        self.navn= str
        self.helse= int
        self.styrke= int
        self.penger= int

    def skap_monster(self):

        monster_liste = {

            'Abdi':[100,20,5],
            'Markus':[120,25,50]
            'Shailesh':[80,30,100000]

        }

    self.navn = random.choice(list(monster_liste))
    attributter = monster_liste.get(self.navn)
    self.helse = attributter[0]
    self.styrke = attributter[1]
    self.penger = attributter[2]
    



        

spiller1=Spiller("Azeem",100,50)

slow_type("Velkommen til Arena 1v1 \n")

while (True):
    break
