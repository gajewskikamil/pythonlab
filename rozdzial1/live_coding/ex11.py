"""
Instukcje warunkowe

Uzupełnij kod tak, aby wykonywał określone zadania
"""

# zapytaj użytkownika o dowolną liczbę, jeśli wartość
# będzie mniejsza od 10 - wypisz dwukrotność podanej
# liczby, jeśli większa od 100 - wypisz jej połowę,
# w każdym innym przypadku wypisz wpisaną wartość
number=int(input("Podaj liczbę: "))
if number<10:
    print(2*number)
elif number>100:
    print(number/2)
else:
    print(number)




# przypisz zmiennej `y` wartość 'dużo' jeśli `x`
# jest większe od 10, w przeciwnym przypadku wartość
# 'mało', użyj jednolinijkowej wersji instrukcji
# warunkowej
x=int(input("podaj x: "))
y="dużo" if x>10 else "mało"
print(y)
