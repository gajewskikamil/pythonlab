"""
Operatory

Uzupełnij kod tak, aby wykonywał określone zadania
"""

# złóż zdanie z podanej listy słów
words = ['Ala', 'ma', 'kota', 'a', 'kot', 'ma', 'Alę']
print(" ".join(words))

# dodaj brakujące słowo (operując na liście) oraz
# odwróć kolejność słów (nie znaków) w podanym zdaniu
sentance = 'Ala ma kota a kot ma'
print((sentance.split() + ["Alę"])[::-1])

# uporządkuj liczby w danej liście w kolejności
# rosnącej
numbers = [100, 12, -52.3, 57, 1, -40, 0, 74]
numbers.sort()
print(numbers)

# uporządkuj liczby w danej liście w kolejności
# rosnącej według wartości bezwzględnej
numbers_abs = [100, 12, -52.3, 57, 1, -40, 0, 74]
numbers_abs.sort(key=abs)
print(numbers_abs)

# dana jest lista ze zwierzętami, zmodyfikuj listę
# tak, aby zawierała jedynie zwierzęta domowe
pets = ['cat', 'snake', 'doge', 'llama', 'hamster']
pets.pop(pets.index('snake'))
pets.pop(pets.index('llama'))
print(pets)
