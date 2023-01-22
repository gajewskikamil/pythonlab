"""
Operatory

Uzupełnij kod tak, aby wykonywał określone zadania
"""

# zapytaj użytkownika o 3 liczby i wypisz ich
# średnią arytmetyczną
#x1=int(input("wpisz liczbe:"))
#x2=int(input("wpisz liczbe:"))
#x3=int(input("wpisz liczbe:"))
#numbers=[x1,x2,x3]
#print(sum(numbers)//len(numbers))

# dana jest godzina `current_hour`, wypisz jaka będzie
# godzina za 17 godzin w systemie 24-godzinnym oraz
# 12-godzinnym
current_hour = 15
future_hour = current_hour + 17
print(future_hour%24)
# cena jednego talerza podana jest w zmiennej `price`,
# a dostępny budżet w zmiennej `budget`, wypisz ile
# talerzy można kupić z podanym budżecie
price = 12
budget = 170

print(budget//price)
