#Miguel Cabezas 10/03/2025
#Dato curioso: esoty pensando seriamente en raparme 
cantantes = ["luismiguel", "chayanne", "davidbisbal, josejose"]

#accede al tercer elemento de la lista 

print(cantantes[3])
#cambia el valor del ultimo elemento

cantantes[-1]="eminem"
#agregar elemento al final de la lista

print(cantantes)
#inserta un elemento en la segunda posicion de la lista
cantantes.append("eminem")
cantantes[2]="luisjara"
#elimina  un elemento de la lista
eliminado = cantantes.pop(4)
#encuentra la posicion de un elemento especifico con .index
indice = cantantes.index("luismiguel")
#ordena la lista de forma alfabetico
cantantes.sort()
#reordenar en reversa
cantantes.reverse()

print(cantantes)
print(eliminado)
print(indice)

