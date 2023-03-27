"""
Funkcje

Uzupełnij kod tak, aby wykonywał określone zadania
"""

# napisz funkcję, która będzie przyjmować argument
# `r` i wypisze obwód i pole koła oraz przetestuj
# napisaną funkcję
import math
def kolo(r):
    print(math.pi*r**2)
    print(2*math.pi*r)
kolo(5)


# napisz funkcję, która będzie przyjmować 2
# argumenty: `text` i `number` i wypisze podany tekst
# powtórzony `number` razy

def boo(text='',number=1):
    print(str(text)*number)

boo("asd",4)
