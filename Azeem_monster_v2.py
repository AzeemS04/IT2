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

spiller = Player("Azeem",100,10)

print(spiller.wallet)

class Monster:
    def __init__(self,name,health,strength,reward):
        self.name=name
        self.health=health
        self.strength=strength
        self.reward=reward

monster1=Monster("Devil",80,20,15)
"lage en metode inne i Monster klassen som lager monster random"


