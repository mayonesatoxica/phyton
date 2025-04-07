#miguel cabezas
#07-04-2025

#instrucciones else

contador = 0

while contador < 10:
    print('contador')
    contador +=1
    
else:
    print('dejo de contar')
    
contador = 0
while contador < 5:
    contador +=1
        
    if (contador == 4):
        print('se rompio el bucle')
        break
    
    print('contador')
    
    contador = 0
    while contador <5:
        contador +=1
        continue
    print(contador)