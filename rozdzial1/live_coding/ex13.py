"""
Pętle

Uzupełnij kod tak, aby wykonywał określone zadania
"""

# dla każdej liczby w podanej liście, wypisz czy
# jest ona podzielna przez 3
numbers = [7, 3, 15, 68, 22, 57, 1, 35, 6]
for i in numbers:
    if i%3==0:
        print(f"{i} jest podzielna przez 3")
    else:
        print(f"{i} nie jest podzielna")


