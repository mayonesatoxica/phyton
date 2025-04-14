#miguel cabezas
#14-04-2025

opciones = [
    ' no persigas la felicidad, creala',
    'todas las cosas son dificiles antes de ser felices',
    'el pajaro madrugador consigue el gusano, pero el segundo raton se lleva el premio',
    'alguien en tu vida necesita una carta de tu parte',
    'no solo pienses, actua',
    'tu corazon se acelera',
    'la fortuna que buscas esta en otra galleta',
    '¡ayuda! ¡estoy prisionero en una panaderia china!'
]

def fortuna():
    import random
    numero = random.randint(0, len(opciones)-1)
    print(opciones[numero])
    

fortuna()
fortuna()
fortuna()
    
    
    