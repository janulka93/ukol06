from random import choice

def hadani(slovo, hadanka):

    print(slovo)
    while True:
        znak = input('Zadej písmeno: ')
        pokus = 0
        #print(len(znak))
        if len(znak) == 1:
            if znak in slovo:
                print('cajk')
                pozice = slovo.index(znak)
                print(pozice, znak)
                hadanka = dopln(hadanka, pozice, znak)
                return hadanka
            else:
                pokus +=  1
                print(pokus, 'počpok')
                vypis(pokus)
                # return pokus
        else:
            print('Zadal jsi číslo nebo řetězec. Zadej nové písmeno.')
            break

def dopln(hadanka, pozice, znak):
    """
    Doplní do řetězce zadané písmeno.
    """
    return hadanka[:pozice] + znak + hadanka[pozice + 1:]

def vypis(pokus):
    """
    Načítá obrázky ze souboru podle čísla pokusu.
    """
    while True:
        nazev = str(pokus) + '.txt'
        soubor = open(nazev, encoding = 'utf-8')
        obrazek = soubor.read()
        soubor.close()
        print(obrazek)
        print(hadanka)
        break


def hraSibenice():
    slovo = choice(("hudba", "slovnik", "pravidlo"))
    hadanka = len(slovo) * '-'
    print(hadanka)
    while slovo != hadanka:
        hadanka = hadani(slovo, hadanka)
        print(hadanka)
    else:
        print('Vyhrála jsi! Hádané slovo je: ', hadanka)


hraSibenice()
