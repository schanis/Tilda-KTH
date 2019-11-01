from HashTable import Hashtable

import timeit

class Song:
    def __init__(self,trackid,latid,artistnamn,lattitel):
        self.trackid=trackid
        self.latid=latid
        self.artistnamn=artistnamn
        self.lattitel=lattitel
    def __str__(self):
        return self.lattitel
    def __lt__(self,other):
        return self.lattitel < other.lattitel
    def __eq__(self, other):
        return self.lattitel == other.lattitel
    #def __gt__(self, other):           #__gt__ behövs inte för att Python är nog tillräckligt smart just här
    #    return self.lattitel > other.lattitel

def hashsokning(q, dinlat):
    #dinlat=input("Ange låt titel: ")
    q.search(dinlat)


def binarsokning(lista, dinlat):

    #dinlat = input("Ange låt titel: ") #ska vara en input
    temp=Song(None,None,None,dinlat)
    start=0
    slut=len(lista)-1
    found=False
    #print(lista[start+slut//2])
    while start<=slut and not found:
        mitten=(start+slut)//2
        if temp == lista[mitten]:
            found=True
            break
        else:
            if temp < lista[mitten]:
                #print(dinlat," mindre ", lista[mitten])
                slut=mitten-1
            else:
                #print(dinlat," större ",lista[mitten])
                start=mitten+1

    return found

def linjarsokning(lista, dinlat):
    for i in lista:
        if i.lattitel == dinlat:
        #print("vi hittade låten")
            return True
    return False

def taketime(n, alist, dinlat):

    lista = alist[0:n]
    print("Antal element =", n)

    linjtid = timeit.timeit(stmt = lambda: linjarsokning(lista, dinlat), number = 100)
    print("Linjärsökning tog", round(linjtid, 4) , "sekunder")
    
    #lista.sort()
    #linjtid = timeit.timeit(stmt = lambda: binarsokning(lista, dinlat), number = 10000)
    #print("Binärsökning tog", round(linjtid, 4) , "sekunder")

    #q=Hashtable(len(lista)*2)
    #for i in lista:
    #    try:
    #        q.store(i.lattitel,i)
    #    except:
    #        pass
    #linjtid = timeit.timeit(stmt = lambda: hashsokning(q, dinlat), number = 100)
    #print("Hashsökning tog", round(linjtid, 4) , "sekunder")


def main():

    lista=[]
    with open("unique_tracks.txt", "r", encoding = "utf-8") as latlista:
        for rad in latlista:
            data = rad.split('<SEP>')
            if data[3].strip()!=None:
                musik=Song(data[0],data[1],data[2],data[3].strip())
                lista.append(musik)
    dinlat = input("Ange låt titel: ")
    taketime(250000,lista, dinlat)
    taketime(500000, lista, dinlat)
    taketime(len(lista), lista, dinlat)

if __name__=='__main__':

    main()