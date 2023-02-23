"""
Operatory

Uzupełnij kod tak, aby wykonywał określone zadania
"""

# dany jest słownik z nazwiskami kierowców F1,
# zmodyfikuj słownik tak, aby pod kluczem z
# nazwiskiem było odpowiednie imię kierowcy
drivers = {
    'Hamilton': '',
    'Verstappen': '',
    'Rosberg': '',
}
drivers["Hamilton"] = "Levis"
drivers["Verstappen"] = "Max"
drivers["Rosberg"] = "Nicko"
print(drivers)



# dany jest słownik ze szczegółami aktora, wypisz
# podsumowanie tych danych w stylu
# "... played in ... as ..."
actor = {
    'movie': 'Fast&Furious',
    'role': 'Dominic Toretto',
    'name': 'Vin Diesel',
}
print(actor['name']+" played in "+actor['movie']+" as "+actor['role'])
