import random
import os
import sys, time

def type(t):
    typing_speed = 500 #wpm
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)



class Spiller:
    def __init__(self,navn,helse,styrke,lommebok):
        self.navn= navn
        self.helse= helse
        self.styrke= styrke
        self.lommebok=lommebok
        

class Monster:
    def __init__(self,navn,helse,styrke,penger):
        self.navn= str
        self.helse= int
        self.styrke= int
        self.penger= int

    def skap_monster(self):

        monster_liste = {

            'Abdi':[100,20,5],
            'Markus':[120,25,50],
            'Shailesh':[80,30,100000]

        }

        self.navn = random.choice(list(monster_liste))
        attributter = monster_liste.get(self.navn)
        self.helse = attributter[0]
        self.styrke = attributter[1]
        self.penger = attributter[2]



def kamp():
    monster = Monster()
    monster.skap_monster()

    type("Monsteret",monster.navn,"har ankommet \n")
    type(f'{monster.navn} har {monster.helse} hp')
    type(f'Kampen starter nå, hva vil du gjøre?')

    while True:
        if monster.helse <= 0:
            type(f'Monsteret har blitt nedkjempet. Du har {spiller.helse} hp igjen')
            spiller.lommebok += monster.penger
            del monster
            break
        type("Hva vil du gjøre?")
        type("Dine valg : \n Slå monsteret [ang], Løp bort [run] \n")
        valg_input= input(":")
        if valg_input == "ang":
            type("Du angriper monsteret")
            monster.helse -= spiller.styrke
            spiller.helse -=monster.styrke

            if monster.helse <= 0:
                pass
            else:
                #print helse til spiller og monster
                pass
        elif valg_input == "run":
            #print du løp, og fikk ingenting
            del monster
            break
        else:
            #skriv på nytt
            pass





type("Hva heter du?")
name = input(":")
spiller = Spiller(name,100,10,0)
