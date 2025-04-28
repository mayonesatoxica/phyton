#Acceder a un valor en un diccionario sin que rompa el programa si la clave no existe

def buscar_cantantes():
    cantantes = {
        "nombre": "luis miguel",
        "pais": "puerto rico"
    }
def buscar_cantantes():
    cantantes = {
        "nombre": "luis miguel",
        "pais": "puerto rico"
    }
    try:
        clave = input("¿Que quieres saber?(nombre o pais):")
        print("Resultado:", cantantes.get(clave, "La clave no existe"))
    except KeyError:
        print("La clave no existe")
    try:
        clave = input("¿Que quieres saber?(nombre o pais):")
        print("Resultado:", cantantes.get(clave, "La clave no existe"))
    except KeyError:
        print("La clave no existe")

buscar_cantantes()

