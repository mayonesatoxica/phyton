#division segura

#objetivo: dividir entre dos numeros y evitar o aletar si al usuario quiere dividir entre 0

def division_segura():
    try:
        num1 = int(input('ingresa un numero:'))
        num2 = int(input('ingresa otro numero:'))
        resultado = num1 / num2
        print('el resultado de la division es:', resultado)
    except ZeroDivisionError:
        print("Error: No se puede dividir entre 0.")
    except ValueError:
        print("Error: Por favor ingresa solo números enteros.")