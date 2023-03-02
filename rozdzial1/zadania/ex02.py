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
print("Wybrałeś: "+gra[you])
computer=choice(range(1,3))
print("Komputer wybrał: "+gra[computer])
match computer:
    case 1:
        print("Remis")
    case 2:
        print("Wygrana")
    case 3:
        print("Przegrana")

#win = "Wygrałeś" if