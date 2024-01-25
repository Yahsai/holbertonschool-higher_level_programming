#!/usr/bin/python3
import random

# Se genera un número aleatorio entre -10000 y 10000
number = random.randint(-10000, 10000)

# Se obtiene el último dígito del número usando el operador % (módulo)
last_digit = abs(number) % 10

# Se imprime el resultado según las condiciones dadas
if number > 0 or last_digit == 0:
    print(f"Last digit of {number} is {last_digit}", end=" ")
else:
    print(f"Last digit of {number} is -{last_digit}", end=" ")

if last_digit > 5 and number > 0:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
