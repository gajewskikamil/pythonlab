"""
Stwórz grę, która zapyta użytkownika o wybór: 'kamień', 'papier' lub 'nożyce'. Następnie wylosuj wybór komputera
i wypisz wynik gry.
"""
from random import choice
gra= {
    1:"Kamień",
    2:"Papier",
    3:"Nożyce"}
you=int(input("1: Kamień \n2: Papier \n3: Nożyce \nWpisz liczbę: "))
computer=choice(range(1,3))
print("Twój wybór: "+gra[you])
print("Komputer wybrał: "+gra[computer]+"\n")
if computer==1:
    match you:
        case 1:
            print("Remis")
        case 2:
            print("Wygrana")
        case 3:
            print("Przegrana")
if computer==2:
    match you:
        case 1:
            print("Przegrna")
        case 2:
            print("Remis")
        case 3:
            print("Wygrana")
if computer==3:
    match you:
        case 1:
            print("Wygrana")
        case 2:
            print("Przegrana")
        case 3:
            print("Remis")