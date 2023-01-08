# Dokumentasjon av Monsterspill prosjekt i Python

I dette prosjektet har jeg jobbet med klasser og objekter

## Filer
[Azeem_monsterspill.py](Azeem_monsterspill.py)

## Azeem_monsterspill.py

Her importerer jeg bibliotekene jeg kan få bruk for til videre bruk i programmet

    from mimetypes import init
    import random
    import os
    import sys, time
    from typing import Type
    
Dette er en funksjon som printer ut tekst til konsollen i en skrivemasking effekt

    def type(t):
    typing_speed = 500 #wpm
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
 
Her definerer jeg klassen Player

    class Player:
        def __init__(self,name,health,strength,wallet = 0):
            self.name=name
            self.health=health
            self.strength=strength
            self.wallet=wallet
            
Her definerer jeg klassen Monster,jeg definerer også en metode som gjør det mulig å spawne et tilfeldig monster.

    class Monster:
        def __init__(self):
            self.name=str
            self.health=int
            self.strength=int
            self.reward=int
            
        def spawn(self):
            monster_dict= {
                'Demon':[100,45,50],
                'Goblin':[50,50,55],
                'Devil':[200,50,50]
            }
            
            self.name=random.choice(list(monster_dict))
            ferdigheter=monster_dict.get(self.name)
            self.health=ferdigheter[0]
            self.strength=ferdigheter[1]
            self.reward=ferdigheter[2]
            
Jeg har valgt å definere en funksjon som heter kamp() som styrer kamp-aspektet av spillet

    def kamp():
        #Spawner monster
        monster=Monster()
        monster.spawn()
        type(f"Du møter på {monster.name} \nMonsteret har {monster.health}hp\n")
        
Inne i kamp funksjonen har jeg en løkke som kjører til enten monsteret har blitt beseiret,spilleren har blitt beseiret eller spiller velger å løpe bort 

        while True:
            #Når monsteret er beseiret
            if monster.health <= 0:
                type("Monsteret har blitt bekjempet\n")
                spiller.wallet += monster.reward
                type(f'Du har tjent {monster.reward} kr\n' )
                type(f'Nå har du {spiller.wallet} kr\n')
                break
            #Når spilleren er beseiret    
            elif spiller.health <= 0:
                type("Du døde \n")
                type("Du mistet alle pengene dine\n")
                type("Du vil nå respawne\n")
                spiller.wallet = 0
                spiller.health=100
                break
                
            #Spilleren får sine valg muligheter
            
            type("Hva vil du gjøre\n")
            type("Slåss[fight] eller løpe bort[run]\n")
            bruker_input=input(":")
            
            #Spilleren valgte å slåss
            if bruker_input == "fight":
                type("Du slo monsteret\n")
                monster.health -= spiller.strength
                if monster.health<=0:
                    pass
                else:
                    spiller.health -= monster.strength
                    if spiller.health <= 0:
                        type(f'Du har 0 hp\nMonsteret har {monster.health} hp igjen\n')
                    else:
                        type(f'Du har {spiller.health}hp\nMonsteret har {monster.health} hp igjen\n')
                        
            #Spilleren valgte å løpe bort
            elif bruker_input == "run":
                type("Du rømte fra monsteret, du får ingenting i premie\n")
                break
                
            #Spilleren skrev inn et ugyldig valg    
            else:
                type("Velg et ordentlig alternativ\n")
                
Her definerer jeg funksjonen for hvordan butikken funker i spillet

     def butikk():
          type("Velkommen til butikken\n Her får du kjøpt våpen og drikker\n")
          type(f'Du har {spiller.wallet} kr \n')
          type("Sting : 15kr (+30hp,+15styrke)")
          type("\nKebab : 50kr (+150hp)\n")
          while True:       #Løkke som kjører frem til du er ferdig i butikken
              type("Hva vil du ha\n")
              type("[sting], [kebab], [tilbake]")
              valg=input(":")
              if valg=="sting":
                  if spiller.wallet>=15:
                      spiller.wallet -= 15
                      type("Du kjøpte Sting\n")
                      spiller.health+=30
                      spiller.strength+=15
                      type(f'Du har {spiller.health}hp og styrke {spiller.strength}\n')
                      type(f'Du har {spiller.wallet}kr igjen')
                  else:
                      type("Du har ikke råd\n")
                      pass
              elif valg=="kebab":
                  if spiller.wallet >=50:
                      spiller.wallet -=50
                      type("Du kjøpte kebab\n")
                      spiller.health +=150
                      type(f'Du har {spiller.health}hp og styrke {spiller.strength}')
                      type(f'Du har {spiller.wallet}kr igjen')
                  else:
                      type("Du har ikke råd\n")
                      pass
              elif valg=="tilbake":
                  break
                  
             
Funksjon som viser inventaret til spilleren

    def inventory():
        type(f'Inventory til spilleren {spiller.name}\n')
        while True:
            type("Hva vil du se?\n")
            type("Lommebok[wallet] , Helse[health], Tilbake[Tilbake]\n ")
            user_choice= input(":")
            if user_choice == "wallet":
                type(f'Lommeboken til {spiller.name}\n')
                type(f'Du har {spiller.wallet} kr\n')
            elif user_choice =="health":
                type(f'Helsen til {spiller.name} er {spiller.health}\n')
            elif user_choice == "tilbake":
                break
                
Hoved funksjonen som gir valg mulighetene til spilleren. Slåss mot monster, sjekke inventaret sitt eller ta en tur innom butikken. Funksjonene over er plassert oppi denne funksjonen.

    #Funksjon hvor spiller velger hva han vil gjøre.
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
            
Hovedløkken hvor hovedfunksjonen vil kjøre i. Før denne funksjonen kjører vil programmet få navnet til spilleren via input og lager et objekt med navnet.

    type("Velkommen til spillet \n")
    type("Hva heter du")
    navn_input=input(": ")
    spiller=Player(navn_input,100,50)

    #Løkken som får spillet til å gå.
    while (True):
        spill()
