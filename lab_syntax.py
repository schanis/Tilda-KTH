from linkedQFile import LinkedQ

class Inmatningsfel(Exception):
    pass

def storeInput(enkel_molekyl):
    q = LinkedQ()
    for i in enkel_molekyl:
        q.enqueue(i)
    q.enqueue(".")
    return q

def readMolekyl(q):
    readAtom(q)
    temp=q.peek()
    if temp.isnumeric():
        readnum(q)
    elif temp==".":
        raise Inmatningsfel("För litet tal")

def readAtom(q):
    readLetter(q)
    symbol = q.peek()
    if symbol.isalpha():
        readletter(q)
    return


def readLetter(q):
    symbol = q.peek()
    x="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if symbol in x:
        q.dequeue()
        return
    else:
        raise Inmatningsfel("Saknad stor bokstav")
    

def readletter(q):
    symbol=q.peek()
    x="abcdefghijklmnopqrstuvwxyz"
    if symbol in x:
        q.dequeue()
        return
    raise Inmatningsfel("Fel på andra bokstav")

def readnum(q):
    number=q.peek()
    if number.isnumeric() and number!="0":
        number=q.dequeue()
        while q.peek().isnumeric():
            number=number + q.dequeue()
        number=int(number)
        if number>=2:
            number=str(number)
            return number
            
        else:
            raise Inmatningsfel("För litet tal")    
    else:
            raise Inmatningsfel("För litet tal")
        

def kollaSyntax(enkel_molekyl):
    q = storeInput(enkel_molekyl)
    try:                                  
        readMolekyl(q)                                 
        return "Formeln är syntaktiskt korrekt"     
    except Inmatningsfel as fel:                            
        return str(fel)


def main():
    enkel_molekyl = input("Ange din atom eller molekyl: ")
    resultat = kollaSyntax(enkel_molekyl)
    print(resultat)
    

if __name__ == '__main__':
    main()
