#miguel cabezas
#30-04-2025

import random

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2

def juego_adivinar():
    total = lanzar_dados()
    print("¡Bienvenido al juego de adivinar el total de los dados!")
    while True:
        try:
            adivinanza = int(input("¿Cuál es el total (2-12)?: "))
            if adivinanza < 2 or adivinanza > 12:
                print("Por favor, ingresa un número entre 2 y 12.")
                continue
            if adivinanza == total:
                print("¡Lo adivinaste!")
                break
            elif adivinanza < total:
                print("El valor es mayor. Intenta de nuevo.")
            else:
                print("El valor es menor. Intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    juego_adivinar()