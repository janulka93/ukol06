from random import randrange

with open('obrazky.txt', encoding='utf-8') as soubor:
    for radek in soubor:
        print(radek[1])


# slovo1 = 'kocka'
# slovo2 = 'hudba'
# slovo3 = 'slovnik'
# slovo4 = 'pravidlo'
# nahoda = randrange(1,4)
# if nahoda == 1:
#     vybrane = slovo1
# elif nahoda == 2:
#     vybrane = slovo2
# elif nahoda == 3:
#     vybrane = slovo3
# elif nahoda == 4:
#     vybrane = slovo4
#
# hadanka = len(vybrane)*'-'
# print(vybrane)
# print(hadanka)
#
# pokus = 0
# while True:
#     znak = input('Které písmeno je v hádaném slově? ')
#     if len(znak) == 1:
#         if znak in vybrane:
#             pozice = vybrane.index(znak)
#             return hadanka
#         else:
#             pokus += 1
#             #printtěchošklivoznaku
#     else:
#         print('Zadej pouze jedno písmeno.')
#
# def dopln(hadanka, pozice, znak):
#     """
#     Doplní do řetězce zadané písmeno (vyskytuje-li se v něm).
#     """
#     return hadanka[:pozice] + znak + hadanka[pozice + 1:]
