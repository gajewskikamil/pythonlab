"""
Instukcje warunkowe

Uzupełnij kod tak, aby wykonywał określone zadania
"""

# zapytaj użytkownika o nazwisko kierowcy F1, a
# następnie wypisz odpowiadający mu zespół,
# w przypadku braku dopasowania wypisz 'brak danych'

surename=input("podaj nazwisko kierowcy F1: ")
match surename:
    case "Verstappen":
        print('Redbull')
    case "Hamilton":
        print('Mercedes')
    case _:
        print("brak danych")