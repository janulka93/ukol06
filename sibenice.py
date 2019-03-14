from random import randrange

prvni = '''






~~~~~~~'''

druhe = '''
+
|
|
|
|
|
~~~~~~~'''

treti = '''
+---.
|
|
|
|
|
~~~~~~~
'''

ctvrte = '''
+---.
|   |
|
|
|
|
~~~~~~~
'''

pate = '''
+---.
|   |
|   O
|
|
|
~~~~~~~
'''

seste = '''
+---.
|   |
|   O
|   |
|
|
~~~~~~~
'''

sedme = '''
+---.
|   |
|   O
| --|
|
|
~~~~~~~
'''

osme = '''
+---.
|   |
|   O
| --|--
|
|
~~~~~~~
'''

devate = '''
+---.
|   |
|   O
| --|--
|  /
|
~~~~~~~
'''

desate = '''
+---.
|   |
|   O
| --|--
|  / \
|
~~~~~~~
'''

slovo1 = 'kocka'
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
    pokus = 0
    print(vybrane)
    while True:
        znak = input('Zadej písmeno: ')
        #print(len(znak))
        if len(znak) == 1:
            if znak in vybrane:
                print('cajk')
                pozice = vybrane.index(znak)
                print(pozice, znak)
                return dopln(hadanka, pozice, znak)
            else:
                pokus += 1
                print(pokus, 'počpok')
                return pokus
        else:
            print('Zadal jsi číslo nebo řetězec. Zadej nové písmeno.')
            break

def vypis(pokus):
    if pokus == 0:
        print()
    elif pokus == 1:
        print(prvni)
    elif pokus == 2:
        print(druhe)
    elif pokus == 3:
        print(treti)
    elif pokus == 4:
        print(ctvrte)
    elif pokus == 5:
        print(pate)
    elif pokus == 6:
        print(seste)
    elif pokus == 7:
        print(sedme)
    elif pokus == 8:
        print(osme)
    elif pokus == 9:
        print(devate)
    elif pokus == 10:
        print(desate)
        print('Konec hry! Došly ti pokusy. Prohrála jsi.')
    else:
        print(hadani(vybrane, hadanka))


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
        print(hadani(vybrane, hadanka))
        # print('pozice jeee', znak)
        # print(dopln(hadanka, pozice, znak))
        vypis(pokus)

hraSibenice()
