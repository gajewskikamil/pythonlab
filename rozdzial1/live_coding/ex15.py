"""
Pętle

Uzupełnij kod tak, aby wykonywał określone zadania
"""

# napisz kod, który dla każdego znaku w podanym
# zdaniu: Jmy Emo Barany Arki Co Poszly Inna Szosa
# wypisze znak, jeśli jest to wielka litera,
# pominie znak, jeśli jest to mała litera,
# zakończy działanie, jeśli jest to cyfra.
# Skorzystaj ze zmiennych `ascii_lowercase`,
# `ascii_uppercase` oraz `digits` modułu `string`

import string

zdanie = "Jmy Emo Baranki Arki Co Poszly Inna Szosa1"

for char in zdanie:
    if char in string.ascii_uppercase:
        print(char, end='')
    elif char in string.ascii_lowercase:
        continue
    elif char in string.digits:
        break

