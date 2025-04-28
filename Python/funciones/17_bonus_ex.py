#Repetir hasta que lo hagan bien, podemos usar un bucle junto con try

def pedir_numero_repetido():
    while True:
        try:
            numero = int(input('Escriba un numero:'))
            print("¡Gracias Tu numero es:", numero)
            break 
        except ValueError:
            print("Por favor, ingrese un número válido.")
pedir_numero_repetido()