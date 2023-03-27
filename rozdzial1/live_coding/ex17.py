"""
Funkcje

Uzupełnij kod tak, aby wykonywał określone zadania
"""

# napisz funkcję, która będzie przyjmowała dowolną
# liczbę argumentów liczbowych i wypisze ich średnią
import math
def sr(*a):
    print(sum(a)/len(a))
sr(1,2,3,4,5,6,7,8,9)


# napisz funkcję `power`, która będzie przyjmowała
# argument pozycyjny `base` oraz argument `expoment`
# z wartością domyślną `2` i będzie wypisywać wartość
# liczby `base` podniesionej do potęgi `exponent`,
# przetestuj funkcję podając jeden oraz oba argumenty

def power(base, expoment=2):
    print(base**expoment)
power(2)
power(2,4)
power(2,expoment=5)