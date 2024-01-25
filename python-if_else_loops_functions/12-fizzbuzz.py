#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        # Verifica si es múltiplo de ambos 3 y 5 primero
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz", end=" ")
        # Luego, verifica si es múltiplo de 3
        elif num % 3 == 0:
            print("Fizz", end=" ")
        # Después, verifica si es múltiplo de 5
        elif num % 5 == 0:
            print("Buzz", end=" ")
        # Si no es múltiplo ni de 3 ni de 5, simplemente imprime el número
        else:
            print(num, end=" ")
