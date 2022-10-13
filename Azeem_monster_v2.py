from mimetypes import init
import random
import os
import sys, time

def type(t):
    typing_speed = 500 #wpm
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)


class Player:
    def __init__(self,name,health,strength,wallet = 0):
        self.name=name
        self.health=health
        self.strength=strength
        self.wallet=wallet



class Monster:
    def __init__(self,name,health,strength,reward):
        self.name=name
        self.health=health
        self.strength=strength
        self.reward=reward

monster1=Monster("Devil",80,20,15)
"lage en metode inne i Monster klassen som lager monster random"


def spill():
    type(f'Velkommen til spillet {spiller.name}\n')
    type("Hva vil du gjøre? \n")
    type("Vil du utforske[utforske], sjekke lommene dine[inventory] eller kjøpe noe fra butikken[butikk]\n")
    user_choice= input(": ")
    valg=["utforske","inventory","butikk"]
    while user_choice not in valg:
        user_choice= input(": ")
        if user_choice=="utforske":
            type("Du tar en spaser tur\n")
            hendelse= random.randint(1,1) #Kan legge til flere hendelser
            if hendelse == 1:
                fight()
        elif user_choice=="inventory":
            inventory()
        elif user_choice=="butikk":
            butikk()
        else:
            type("Skriv et gyldig valg\n")
            type("Vil du utforske[utforske], sjekke lommene dine[inventory] eller kjøpe noe fra butikken[butikk]\n")









type("Velkommen til spillet \n")
type("Hva heter du")
navn_input=input(": ")
spiller=Player(navn_input,100,10)

while (True):
    spill()

