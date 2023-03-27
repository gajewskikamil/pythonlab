"""
Funkcje

Uzupełnij kod tak, aby wykonywał określone zadania
"""


# napisz fukcję, która będzie przyjmowała jeden
# argument - temperaturę w stopniach Celsjusza
# i będzie zwracała temperaturę w stopniach
# Fahrenheita
# (0°C × 9/5) + 32 = 32°F
def tem(stopnieC):
    f=stopnieC * 9 / 5 + 32
    return f
print(tem(40))


# napisz fukcję, która będzie przyjmowała dwa
# argumenty - cenę netto jako argument obowiązkowy
# oraz wysokość podatku z domyślną wartością `0.23`
# i będzie zwracała cenę butto
def na_brutto(netto, podatek=0.23):
    brutto = netto + netto * podatek
    return brutto
print(na_brutto(5000))

# napisz funcję, która będzie przyjmowała jeden
# argument - cenę w PLN i zwracała cenę w USD,
# przyjmij przelicznik na poziomie 1 PLN = 4.14 USD
def pl_na_usd(cena):
    usd=cena*4.14
    return usd
print(pl_na_usd(20))


# napisz funkcję, która będzie przyjmowała jeden
# argument - cenę netto w PLN i będzie zwracała cenę
# brutto w USD - wykorzystaj funkcje z poprzednich
# zadań

def plnusd(netto):
    return na_brutto(pl_na_usd(netto))
print(plnusd(10))
