from random import randrange

slovo1 = 'rymicka'
slovo2 = 'hudba'
slovo3 = 'slovnik'
slovo4 = 'pravidlo'
pocetSlov = 4

def vyberSlova(pocetSlov):
    '''Vybere hádané slovo. '''
    nahoda = randrange(1,pocetSlov)
    if nahoda == 1:
        vybrane = slovo1
        return vybrane
    elif nahoda == 2:
        vybrane = slovo2
        return vybrane
    elif nahoda == 3:
        vybrane = slovo3
        return vybrane
    elif nahoda == 4:
        vybrane = slovo4
        return vybrane

def hadani(vybrane, hadanka):
    # pokus = 0
    print(vybrane)
    while True:
        znak = input('Zadej písmeno: ')
        pokus = 0
        #print(len(znak))
        if len(znak) == 1:
            if znak in vybrane:
                print('cajk')
                pozice = vybrane.index(znak)
                print(pozice, znak)
                hadanka = dopln(hadanka, pozice, znak)
                return hadanka
            else:
                pokus += 1
                pokSoubor = str(pokus) + '.txt'
                print(pokSoubor)
                print(pokus, 'počpok')
                vypis(pokus)
                # return pokus
        else:
            print('Zadal jsi číslo nebo řetězec. Zadej nové písmeno.')
            break

def vypis(pokusSoubor):
    for pokus in range(0,10)
        if pokusSoubor >= 1 and pokusSoubor < 10:
            soubor = open(pokusSoubor, encoding = 'utf-8')
            obrazek = soubor.read()
            soubor.close()
            print(obrazek)
        elif pokusSoubor == 10:
            soubor = open('10.txt', encoding = 'utf-8')
            obrazek = soubor.read()
            soubor.close()
            print(obrazek)
            print('Konec hry! Prohrála jsi. Hádané slovo: ', vybrane)

def dopln(hadanka, pozice, znak):
    """
    Doplní do řetězce zadané písmeno (vyskytuje-li se v něm).
    """
    return hadanka[:pozice] + znak + hadanka[pozice + 1:]

def hraSibenice():
    vybrane = vyberSlova(pocetSlov)
    print(vyberSlova(pocetSlov))
    hadanka = '_'*len(vybrane)
    print(hadanka)
    while vybrane != hadanka:
        hadanka = hadani(vybrane, hadanka)
        print(hadanka)
        # print('pozice jeee', znak)
        # print(dopln(hadanka, pozice, znak))
    else:
        print('Vyhrála jsi! Hádané slovo je: ', vybrane)


hraSibenice()
