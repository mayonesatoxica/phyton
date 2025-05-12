#miguel cabezas
#12-05-2025

# Actualizar valores en diccionarios y listas

matriz = [[10, 15, 20], [3, 7, 14]]
matriz[1][0] = 6

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
cantantes[0]["nombre"] = "Enrique Martin Morales"

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
ciudades["México"][2] = "Monterrey"

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
coordenadas[0]["latitud"] = 9.9355431

# Iterar a través de una lista de diccionarios
def iterarDiccionario(lista):
    for diccionario in lista:
        print(", ".join(f"{llave} - {valor}" for llave, valor in diccionario.items()))

# Obtener valores de una lista de diccionarios
def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])

# Iterar a través de un diccionario con valores de lista
def imprimirInformacion(diccionario):
    for clave, valores in diccionario.items():
        print(f"{len(valores)} {clave.upper()}")
        for valor in valores:
            print(valor)

print("Iterar Diccionario:")
iterarDiccionario(cantantes)

print("\nIterar Diccionario2:")
iterarDiccionario2("nombre", cantantes)

print("\nImprimir Información:")
imprimirInformacion(ciudades)