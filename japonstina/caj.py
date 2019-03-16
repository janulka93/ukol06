#načtení souboru a uložení textového obsahu
with open('rozsypanycaj.txt', encoding='utf-8') as soubor:
    caj = soubor.read()
with open('hiragana.txt', encoding='utf-8') as soubor:
    hiragana = soubor.read()
with open('katakana.txt', encoding='utf-8') as soubor:
    katakana = soubor.read()


def pocitani_znaku(abeceda, text):
    '''Funkce prochází text a srovnává jej se znaky abecedy.
    Na závěr je vypisován počet znaků dané abecedy vyskytujících se v textu.'''
    pocet = 0
    for i in range(len(text)):
        for j in range(len(abeceda)):
            if abeceda[j] in text[i]:
                if abeceda[j] == ' ' or abeceda[j] == '\n': #ošetření, aby se nezapočítávaly i mezery
                    break
                else:
                    pocet += 1
    return pocet

print('V zadaném textu je', pocitani_znaku(hiragana, caj), 'znaků hiragany.')
print('V zadaném textu je', pocitani_znaku(katakana, caj), 'znaků katakany.')
