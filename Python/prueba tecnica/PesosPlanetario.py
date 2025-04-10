#miguel cabezas
#09-04-2025

Peso = float(input('¿Cuantos pesas?'))

peso_usuario = int(input('¿Cuál es tu peso terrestre? (1)mercurio (2)venus (3)marte (4)jupiter (5)saturno (6)urano (7) neptuno'))

if peso_usuario == 1:
    print(f'Tu peso en Mercurio sería: {Peso * 0.38} kg')
elif peso_usuario == 2:
    print(f'Tu peso en Venus sería: {Peso * 0.91} kg')
elif peso_usuario == 3:
    print(f'Tu peso en Marte sería: {Peso * 0.38} kg')
elif peso_usuario == 4:
    print(f'Tu peso en Júpiter sería: {Peso * 2.53} kg')
elif peso_usuario == 5:
    print(f'Tu peso en Saturno sería: {Peso * 1.07} kg')
elif peso_usuario == 6:
    print(f'Tu peso en Urano sería: {Peso * 0.89} kg')
elif peso_usuario == 7:
    print(f'Tu peso en Neptuno sería: {Peso * 1.14} kg')
else:
    print('Numero de polaneta no valido')