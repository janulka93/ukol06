print('''Tento program slouží ke kopírování souborů.
Názvy zadávej ručně a nezapomeň na příponu!!!
''')

while True:
    nazevPred = input('Zadej název otevíraného souboru: ')

    if '.' in nazevPred:
        try:
            soubor = open(nazevPred, encoding='utf-8')
        except FileNotFoundError:
            print('Takový soubor neexistuje!')
        else:
            obsah = soubor.read()
            nazevPo = input('Zadej název nového souboru: ')
            if '.' in nazevPo:
                soubor = open(nazevPo, mode = 'w', encoding='utf-8')
                print(obsah, file=soubor)
                soubor.close()
                print('Byl vytvořen nový soubor:', nazevPo)
                break
            else:
                print('Chybí ti přípona!')
    else:
        print('Chybí ti přípona souboru!')
