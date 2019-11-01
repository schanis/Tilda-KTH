class Node:  # Noder till klassen Hashtable

    def __init__(self, key="", data=None):  # key: nyckeln som anvands vid hashningen      data: det objekt som ska hashas in
        self.key = key
        self.data = data


class Hashtable:

    def __init__(self, size):  # """size: hashtabellens storlek"""
        self.size = size
        self.slot = [None] * self.size
        self.data = [None] * self.size


    def store(self, member):
        hashvalue = self.hashfunction(member.key)

        if self.slot[hashvalue] == None:  # en ny objekt sparas i hashtabellen
            self.slot[hashvalue] = member.key()
            self.data[hashvalue] = member.data()
        else:  # slot är upptaget och vi letar ett nytt (nästa möjliga), linjär probning
            nextslot = self.rehash(hashvalue)
            while self.slot[nextslot] != None:
                nextslot = self.rehash(nextslot)
            self.slot[nextslot] = member.key  # Stoppar in "data" med nyckeln "key" i tabellen.
            self.data[nextslot] = member.data

    def search(self, key):  # """key: nyckeln
        # Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
        # ej färdigt
        pass
        # Om "key" inte finns ska vi få en Exception, KeyError """


    def hashfunction(self,key):  # Beräknar hashfunktionen för key"""
        index_string = ""
        for letter in key:
            number = ord(letter) * 31  # multipricerar kod med ett primtal, 31 av tradition ;)
            code = str(number)
            index_string += code
            # print(letter, code, index_string)
        big_index = int(index_string)
        decent_index = big_index % self.size
        return decent_index


    def rehash(self, oldhash):
        return (oldhash + 1) % self.size()


# Class Pokemon är från lab 1, det är direkt kopierat för att underlätta när vi ska läsa in från fil och lagra det i vår Hashtabell.
class Pokemon:
    def __init__(self, Name, Type1, Type2, Total, HP, Attack, Defense, SpAtk, SpDef, Speed, Generation, Legendary):
        self.Name = Name
        self.Type1 = Type1
        self.Type2 = Type2
        self.Total = Total
        self.HP = HP
        self.Attack = Attack
        self.Defense = Defense
        self.SpAtk = SpAtk
        self.SpDef = SpDef
        self.Speed = Speed
        self.Generation = Generation
        self.Legendary = Legendary

    def __str__(self):  # Gör om objekt data till Sträng så vi enkelt kan avläsa och använda datan

        return 'Name: {self.Name}\nType 1: {self.Type1}\nType 2: {self.Type2}\nTotal:{self.Total}\nHP:{self.HP}\nAttack:{self.Attack}\nDefense:{self.Defense}\nSpAtk:{self.SpAtk}\nSpDef{self.SpDef}\nSpeed:{self.Speed}\nGeneration:{self.Generation}\nLegendary:{self.Legendary}'.format(
            self=self)


def hamta():  # Läser in filen
    fil = "pokemon.csv"
    pokelist = Hashtable(1601)
    with open(fil, encoding="utf-8") as pokemonfil:
        for rad in pokemonfil:
            x = rad.split(",")
            namn = x[1]
            Type1 = x[2]
            Type2 = x[3]
            Total = x[4]
            HP = x[5]
            Attack = x[6]
            Defense = x[7]
            SpAtk = x[8]
            SpDef = x[9]
            Speed = x[10]
            Generation = x[11]
            Legendary = x[12].strip("\n")

            p = Pokemon(namn, Type1, Type2, Total, HP, Attack, Defense, SpAtk, SpDef, Speed, Generation, Legendary)
            pokelist.store(p)

    return pokelist

def main():
    q=Hashtable(10)
    print(q.size)
    #q.store()
main()