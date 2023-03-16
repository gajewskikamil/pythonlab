"""
Pętle

Uzupełnij kod tak, aby wykonywał określone zadania
"""

# zapytaj użytkownika o podanie liczby i zapisz jego
# wybór do listy, następnie pytaj o kolejną liczbę,
# dopóki nie poda 0, na koniec wypisz średnią wartość
# wszystkich podanych przez użytkownika liczb
numbers=None
n=[]
while numbers!=0:
    numbers = int(input("Podaj liczbę: "))
    if numbers!=0:
        n.append(numbers)
print(sum(n) / len(n))