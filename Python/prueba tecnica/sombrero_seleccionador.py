#miguel cabezas
#09-04-2025

casas = ['Gryffindor, Hufflepuff, Slytherin, Revenclaw']

pregunta1 = input('¿Te gusta mas el amanecer o el atardecer?')

if pregunta1.lower() == 'amanecer':
    print('¡1 punto para Gryffindor!')
elif pregunta1.lower() == 'atardecer':
    print('¡1 punto para Hufflepuff y Slytherin!')
else:
    print('Entrada incorrecta.')

pregunta2 = input('Cuando quiero que la gente me recuerde como:')

if pregunta2.lower() == 'el bueno':
    print('¡2 puntos para Hufflepuff!')

elif pregunta2.lower() == 'el mal':
    print('¡2 puntos para Slytherin!')
    
elif pregunta2.lower() == 'el grandioso':
    print('¡2 puntos para Revenclaw!')
    
elif pregunta2.lower() == 'el valiente':
    print('¡2 puntos para Gryffindor!')
else:
    print('Entrada incorrecta.')
    
pregunta3 = input('Qué tipo de instrumento complace mas tu oido?')

if pregunta3.lower() == 'el violin':
    print('¡4 puntos para Slytherin!')

elif pregunta3.lower() == 'la trompeta':
    print('¡4 puntos para Hufflepuf!')
    
elif pregunta3.lower() == 'el piano':
    print('¡4 puntos para Revenclaw!')
    
elif pregunta3.lower() == 'el tambor':
    print('¡4 puntos para Gryffindor!')
else:
    print('Entrada incorrecta.')
    
    