"""
Instukcje warunkowe

Uzupełnij kod tak, aby wykonywał określone zadania
"""

# zapytaj użytkownika o nazwisko kierowcy F1, a
# następnie wypisz odpowiadający mu zespół,
# w przypadku braku dopasowania wypisz 'brak danych'
drivers = {
    "Verstappen": "RedBull",
    "Hamilton": "Mercedes",
}
surename=input("podaj nazwisko kierowcy F1: ")
match surename:
    case "Verstappen":
        print(drivers[surename])
    case "Hamilton":
        print(drivers[surename])
    case none:
        print("brak danych")