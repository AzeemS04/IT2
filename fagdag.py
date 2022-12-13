

class Vare:
    def __init__(self,kategori,underkategori,pristype,pris,mengde):
        self.kategori=kategori
        self.underkategori=underkategori
        self.pristype=pristype
        self.pris=pris
        self.mengde=mengde

    def prisBetale(self):
        return self.mengde * self.pris


def handle():

    print("Hva vil du kjøpe?")
    print("epler (Pink) koster 20 kr pr kg")
    print("appelsiner (Jaffa) koster 25 kr pr kg")
    print("ananas (hel) koster kr 15 pr stk")
    print("")
    print("Skriv epler,appelsiner eller ananas")
    print("")
    print("Hvis du er ferdig skriv, ferdig")
    valg=input(":")
    if valg == "epler":
        print("Hvor mye skal du ha? Oppgi i heltall")
        mengde=int(input(": "))
        vare1= Vare("epler","pink","pr kg",20,mengde)

        print("Prisen å betale er", vare1.prisBetale())
        return vare1.prisBetale()
    elif valg == "appelsiner":
        print("Hvor mye skal du ha? Oppgi i heltall")
        mengde=int(input(": "))
        vare1= Vare("appelsiner","jaffa","pr kg",25,mengde)

        print("Prisen å betale er", vare1.prisBetale())
        return vare1.prisBetale()
    elif valg == "ananas":
        print("Hvor mye skal du ha? Oppgi i heltall")
        mengde=int(input(": "))
        vare1= Vare("ananas","hel","pr stk",15,mengde)
        
        print("Prisen å betale er", vare1.prisBetale())
        return vare1.prisBetale()
    elif valg == "ferdig":
        print(f'Totalsummen din ble {totalsum}')
        return False



totalsum=0
while(True):
    handling=handle()
    if handling == False:
        break
    else:
        totalsum += handling
        print(totalsum)
        continue
