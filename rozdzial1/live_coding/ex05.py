"""
Operatory

Uzupełnij kod tak, aby wykonywał określone zadania
"""

# portal wymaga podania nazwy użytkownika, zapytaj
# użytkownika o jego imię, nazwisko oraz dowolną
# liczbę, a następnie utwórz nazwę użytkownika w stylu
# ImięNazwiskoLiczba
user_name = input('What your name?:')
user_surname = input('What your surname?:')
number = int(input("gi mi number:"))
print("Your username -",user_name.title()+user_surname.title()+str(number))


# utwórz nazwę użytkownika jak wyżej, ale pisane od
# tyłu, tj: ĘimiOksiwzanAbzcil

print("Your username -",user_surname[::-1].title()+user_name[::-1].title()+str(number))