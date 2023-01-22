"""
Operatory

Uzupełnij kod tak, aby wykonywał określone zadania
"""

# zapytaj użytkownika o liczbę i wypisz czy jest
# ona większa od zmiennej `number`
number = 24
x=input("wpisz liczbe:")
print(int(x)>number)


# zapytaj użytkownika o 3 liczby i wypisz czy któraś
# z nich ma taką samą wartość, jak zmienna `number`

a1=input("wpisz liczbe:")
a2=input("wpisz liczbe:")
a3=input("wpisz liczbe:")
l=[int(a1),int(a2),int(a3)]
print(number in l)
