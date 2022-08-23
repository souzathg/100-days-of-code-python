import random

# Fazendo a importação do módulo
import my_module

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random() * 5 # Expanding the range from 0-1 to 0-5.
print(random_float)

# Usando a importação do módulo
print(my_module.pi)

love_score = random.randint(1, 100)
print(f"Your love socre is {love_score}.")
