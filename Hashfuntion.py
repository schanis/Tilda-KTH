def hashC(ortsnamn):
    s = ""
    for bokstav in ortsnamn:
        nummer = ord(bokstav)
        kod = str(nummer)
        s += kod
        #print(bokstav, kod, s)
    storttal = int(s)
    lagomtal = storttal % 250000
    return lagomtal
def main():
    index = hashC("Stockholm")
    print("Stoppa in i hashtabellen på plats", index)
main()
