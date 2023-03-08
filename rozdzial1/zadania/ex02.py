"""
Stwórz grę, która zapyta użytkownika o wybór: 'kamień', 'papier' lub 'nożyce'. Następnie wylosuj wybór komputera
i wypisz wynik gry.
"""
from random import choice

gra = {
    1: "Kamień",
    2: "Papier",
    3: "Nożyce"}
you = int(input("1: Kamień \n2: Papier \n3: Nożyce \nWpisz liczbę: "))
computer = choice(range(1, 3))
print("Twój wybór: " + gra[you])
print("Komputer wybrał: " + gra[computer] + "\n")

if computer==you:
    print("Remis")
elif computer == 3 and you == 1 or computer == 2 and you == 3 or computer == 1 and you == 2:
    print("Wygrana")
else:
    print("Przegrana")
def exe3():
    if computer != you:
        if computer != 1:
            if computer != 2:
                print("Wygrana") if you == 1 else print("Przegrana")
            else:
                print("Wygrana") if you == 3 else print("Przegrana")
        else:
            print("Wygrana") if you == 2 else print("Przegrana")
    else:
        print("Remis")
def exe2():
    if you == computer:
        print("Remis")
    else:
        if computer == 1:
            if you == 2:
                print("Wygrana")
            else:
                print("Przegrana")
        else:
            if computer == 2:
                if you == 1:
                    print("Przegrana")
                else:
                    print("Wygrana")
            else:
                if you == 2:
                    print("Przegrana")
                else:
                    print("Wygrana")
def exe():
    if computer == 1:
        match you:
            case 1:
                print("Remis")
            case 2:
                print("Wygrana")
            case 3:
                print("Przegrana")
    if computer == 2:
        match you:
            case 1:
                print("Przegrana")
            case 2:
                print("Remis")
            case 3:
                print("Wygrana")
    if computer == 3:
        match you:
            case 1:
                print("Wygrana")
            case 2:
                print("Przegrana")
            case 3:
                print("Remis")

