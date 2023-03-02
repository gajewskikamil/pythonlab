"""
Stwórz grę, która zapyta użytkownika o wybór: 'kamień', 'papier' lub 'nożyce'. Następnie wylosuj wybór komputera
i wypisz wynik gry.
"""
from random import choice
you=int(input("1: Kamień \n2: Papier \n3: Nożyce \nWpisz liczbę"))

k="Kamień"
p="Papier"
n="Nożyce"
computer=choice(k,p,n)
print(you)
#win = "Wygrałeś" if