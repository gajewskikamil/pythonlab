"""
Importowanie

Uzupełnij kod tak, aby wykonywał określone zadania
"""
from random import choice

# dana jest lista Pokemonów, napisz kod, który zapyta
# co to za Pokemon, a następnie wylosuje dowolnego z
# listy, zaimportuj odpowiednią bibliotekę
pokemons = ['Psyduck', 'Ivysaur', 'Spearow', 'Pikachu']
htp=input('co to za pokemon?: ')
htp=pokemons.index(htp)
poks=choice(range(0,len(pokemons)))
if(pokemons[htp]==pokemons[poks]):
    print("yes, it's "+pokemons[poks])
else:
    print("no, it's "+pokemons[poks]+", fuuuuuuck")

# zaimportuj oraz wypisz zawartość zmiennej `element`
# znajdującej się w paczce `package` oraz zmiennej
# `element` znajdującej się w module `module` paczki
# `package`
import package

# wypisz wartość zmiennej `pi` znajdującej się w
# paczce `math`
