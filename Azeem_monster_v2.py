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

monster1=Monster("Devil",80,5,15)
#lage en metode inne i Monster klassen som lager monster random"


def kamp():
    type("Du møter på et monster\n")
    type(f'{monster1.name} har {monster1.health} hp\n')
    type(f'Du har {spiller.health} hp\n')

    while True:
        if monster1.health <= 0:
            type("Monsteret har blitt bekjempet\n")
            spiller.wallet += monster1.reward
            type(f'Du har tjent {monster1.reward}\n' )
            type(f'Nå har du {spiller.wallet} kr\n')
            break
        type("Hva vil du gjøre\n")
        type("Slåss[fight] eller løpe bort[run]\n")
        bruker_input=input(":")
        if bruker_input == "fight":
            type("Du slo monsteret\n")
            monster1.health -= spiller.strength
            spiller.health -= monster1.strength
            if monster1.health<=0:
                pass
            else:
                type(f'Du har {spiller.health}hp\nMonsteret har {monster1.health} hp igjen\n')

        elif bruker_input == "run":
            type("Du rømte fra monsteret, du får ingenting i premie\n")
            break
        else:
            type("Velg et ordentlig alternativ\n")

"""    type("Hva vil du gjøre\n")
    type("Slåss[fight] eller løpe bort[run]")
    bruker_input=input(":")
    handlinger=["fight","run"]
    if bruker_input == "fight":
        type("Du angrep monsteret")
        monster1.health -= spiller.strength
        type(f'Monsteret ble skadet.\n Monsteret har {monster1.health} hp igjen')
    else:
        type("Skriv et gyldig valg\n")
        type("Slåss[fight] eller løpe bort[run]\n")"""


def spill():
    type("Hva vil du gjøre? \n")
    type("Vil du utforske[utforske], sjekke lommene dine[inventory] eller kjøpe noe fra butikken[butikk]\n")
    user_choice= input(": ")
    valg=["utforske","inventory","butikk"]
    if user_choice=="utforske":
        type("Du tar en spaser tur\n")
        hendelse= random.randint(1,1) #Kan legge til flere hendelser
        if hendelse == 1:
            kamp()
    elif user_choice=="inventory":
        inventory()
    elif user_choice=="butikk":
        butikk()
    else:
        type("Skriv et gyldig valg\n")





type("Velkommen til spillet \n")
type("Hva heter du")
navn_input=input(": ")
spiller=Player(navn_input,100,50)

while (True):
    spill()

