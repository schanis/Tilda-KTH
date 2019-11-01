class DictHash:

    def __init__(self):
        self.dict=dict()

    def __str__(self):
        return '{self.dict}'.format(self=self)

    def store(self,key,value):    #lagrar data som value i din dictionary, med nyckel som key.
        self.dict[key]=value

    def search(self,key): # x = search(nyckel) som slår upp nyckel i din dictionary. returnerar data
        try:
            return self.dict[key]
        except:
            return None
    
    def __getitem__(self,nyckel):  # ej testat
        return self.search(nyckel)
    
    def __contains__(self, nyckel):  # ej testat
        finns = False
        if self.search(nyckel) != None:
            finns = True
        return finns


class Pokemon:
    def __init__(self,Name,Type1, Type2, Total, HP, Attack, Defense, SpAtk, SpDef, Speed, Generation,Legendary):
        self.Name=Name
        self.Type1=Type1
        self.Type2=Type2
        self.Total=Total
        self.HP=HP
        self.Attack=Attack
        self.Defense=Defense
        self.SpAtk=SpAtk
        self.SpDef=SpDef
        self.Speed=Speed
        self.Generation=Generation
        self.Legendary=Legendary
        
    def __str__(self): #Gör om objekt data till Sträng så vi enkelt kan avläsa och använda datan

        return 'Name: {self.Name}\nType 1: {self.Type1}\nType 2: {self.Type2}\nTotal:{self.Total}\nHP:{self.HP}\nAttack:{self.Attack}\nDefense:{self.Defense}\nSpAtk:{self.SpAtk}\nSpDef{self.SpDef}\nSpeed:{self.Speed}\nGeneration:{self.Generation}\nLegendary:{self.Legendary}'.format(self=self)

    
#allt under är från lab 1, det är direkt kopierat för att underlätta när vi ska läsa in från fil och lagra det i vår DictHash.

def hamta(): # Läser in filen
    fil = "pokemon.csv"
    pokelist=DictHash()
    with open(fil,encoding= "utf-8") as pokemonfil:
        for rad in pokemonfil:
            x=rad.split(",")
            namn=x[1]
            Type1=x[2]
            Type2=x[3]
            Total=x[4]
            HP=x[5]
            Attack=x[6]
            Defense=x[7]
            SpAtk=x[8]
            SpDef=x[9]
            Speed=x[10]
            Generation=x[11]
            Legendary=x[12].strip("\n")

            p = Pokemon(namn,Type1,Type2 ,Total, HP, Attack, Defense, SpAtk, SpDef, Speed, Generation,Legendary)

            pokelist.store(namn,p)

    return pokelist

pokelist = hamta()
print (pokelist["Bulbasaur"])
print (pokelist["Abc"])