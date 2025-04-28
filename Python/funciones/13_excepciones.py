#miguel cabezas
#28-04-2025
#ejercicio 1 convension segura a numero 
#objetivo: pedir un numero al usuario y evitar errores si escribe letras.

def pedir_numero():
    try:
        numero = int(input('escribe un numero entero:'))
        print("¨¡Gracias! Tu numero es:", numero)
    except ValueError:
        print("Eso no es un numero valido. Intenta otra vez.")

        pedir_numero()